// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

#pragma once

#include <assert.h>
#include <glog/logging.h>
#include <stdint.h>
#include <string.h>

#include <algorithm>
#include <memory>
#include <ostream>
#include <utility>
#include <vector>

#include "common/status.h"
#include "olap/decimal12.h"
#include "olap/uint24.h"
#include "runtime/collection_value.h"
#include "util/slice.h"
#include "vec/columns/column.h"
#include "vec/columns/column_nullable.h"
#include "vec/columns/column_string.h"
#include "vec/columns/column_variant.h"
#include "vec/columns/column_vector.h"
#include "vec/common/assert_cast.h"
#include "vec/common/pod_array_fwd.h"
#include "vec/common/string_ref.h"
#include "vec/core/column_with_type_and_name.h"
#include "vec/core/types.h"
#include "vec/data_types/data_type.h"
#include "vec/data_types/data_type_array.h"
#include "vec/data_types/data_type_factory.hpp"
#include "vec/data_types/data_type_map.h"
#include "vec/data_types/data_type_variant.h"

namespace doris {

class TabletSchema;
class TabletColumn;

namespace vectorized {

class Block;
class ColumnArray;
class ColumnMap;
class DataTypeMap;
template <PrimitiveType T>
class ColumnDecimal;

class IOlapColumnDataAccessor {
public:
    virtual const UInt8* get_nullmap() const = 0;
    virtual const void* get_data() const = 0;
    virtual const void* get_data_at(size_t offset) const = 0;
    virtual ~IOlapColumnDataAccessor() = default;
};

class OlapBlockDataConvertor {
public:
    OlapBlockDataConvertor() = default;
    OlapBlockDataConvertor(const TabletSchema* tablet_schema);
    OlapBlockDataConvertor(const TabletSchema* tablet_schema, const std::vector<uint32_t>& col_ids);
    void set_source_content(const vectorized::Block* block, size_t row_pos, size_t num_rows);
    Status set_source_content_with_specifid_columns(const vectorized::Block* block, size_t row_pos,
                                                    size_t num_rows, std::vector<uint32_t> cids);
    Status set_source_content_with_specifid_column(const ColumnWithTypeAndName& typed_column,
                                                   size_t row_pos, size_t num_rows, uint32_t cid);

    void clear_source_content();
    std::pair<Status, IOlapColumnDataAccessor*> convert_column_data(size_t cid);
    void add_column_data_convertor(const TabletColumn& column);

    bool empty() const { return _convertors.empty(); }
    void reserve(size_t size) { _convertors.reserve(size); }
    void reset() { _convertors.clear(); }

private:
    class OlapColumnDataConvertorBase;

    using OlapColumnDataConvertorBaseUPtr = std::unique_ptr<OlapColumnDataConvertorBase>;
    using OlapColumnDataConvertorBaseSPtr = std::shared_ptr<OlapColumnDataConvertorBase>;

    static OlapColumnDataConvertorBaseUPtr create_olap_column_data_convertor(
            const TabletColumn& column);
    static OlapColumnDataConvertorBaseUPtr create_map_convertor(const TabletColumn& column);
    static OlapColumnDataConvertorBaseUPtr create_array_convertor(const TabletColumn& column);
    static OlapColumnDataConvertorBaseUPtr create_struct_convertor(const TabletColumn& column);
    static OlapColumnDataConvertorBaseUPtr create_agg_state_convertor(const TabletColumn& column);

    // accessors for different data types;
    class OlapColumnDataConvertorBase : public IOlapColumnDataAccessor {
    public:
        OlapColumnDataConvertorBase() = default;
        ~OlapColumnDataConvertorBase() override = default;
        OlapColumnDataConvertorBase(const OlapColumnDataConvertorBase&) = delete;
        OlapColumnDataConvertorBase& operator=(const OlapColumnDataConvertorBase&) = delete;
        OlapColumnDataConvertorBase(OlapColumnDataConvertorBase&&) = delete;
        OlapColumnDataConvertorBase& operator=(OlapColumnDataConvertorBase&&) = delete;

        virtual void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                                       size_t num_rows);
        void clear_source_column();
        const UInt8* get_nullmap() const override;
        virtual Status convert_to_olap() = 0;

    protected:
        ColumnWithTypeAndName _typed_column;
        size_t _row_pos = 0;
        size_t _num_rows = 0;
        const UInt8* _nullmap = nullptr;
    };

    class OlapColumnDataConvertorObject : public OlapColumnDataConvertorBase {
    public:
        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        const void* get_data() const override;
        const void* get_data_at(size_t offset) const override {
            throw doris::Exception(ErrorCode::NOT_IMPLEMENTED_ERROR,
                                   "OlapColumnDataConvertorObject not support get_data_at");
        }

    protected:
        PaddedPODArray<Slice> _slice;
        PaddedPODArray<char> _raw_data;
    };

    class OlapColumnDataConvertorHLL final : public OlapColumnDataConvertorObject {
    public:
        Status convert_to_olap() override;
    };

    class OlapColumnDataConvertorBitMap final : public OlapColumnDataConvertorObject {
    public:
        Status convert_to_olap() override;
    };

    class OlapColumnDataConvertorQuantileState final : public OlapColumnDataConvertorObject {
    public:
        Status convert_to_olap() override;
    };

    class OlapColumnDataConvertorChar : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorChar(size_t length);
        ~OlapColumnDataConvertorChar() override = default;

        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        const void* get_data() const override;
        const void* get_data_at(size_t offset) const override;
        Status convert_to_olap() override;

    private:
        static bool should_padding(const ColumnString* column, size_t padding_length) {
            // Check sum of data length, including terminating zero.
            return column->size() * padding_length != column->chars.size();
        }

        static ColumnPtr clone_and_padding(const ColumnString* input, size_t padding_length) {
            auto column = vectorized::ColumnString::create();
            auto padded_column =
                    assert_cast<vectorized::ColumnString*>(column->assume_mutable().get());

            column->offsets.resize(input->size());
            column->chars.resize(input->size() * padding_length);
            memset(padded_column->chars.data(), 0, input->size() * padding_length);

            for (size_t i = 0; i < input->size(); i++) {
                column->offsets[i] = (i + 1) * padding_length;

                auto str = input->get_data_at(i);

                DCHECK(str.size <= padding_length)
                        << "char type data length over limit, padding_length=" << padding_length
                        << ", real=" << str.size;

                if (str.size) {
                    memcpy(padded_column->chars.data() + i * padding_length, str.data, str.size);
                }
            }

            return column;
        }

        size_t _length;
        PaddedPODArray<Slice> _slice;
        ColumnPtr _column = nullptr;
    };

    class OlapColumnDataConvertorVarChar : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorVarChar(bool check_length, bool is_jsonb = false);
        ~OlapColumnDataConvertorVarChar() override = default;

        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        const void* get_data() const override;
        const void* get_data_at(size_t offset) const override;
        Status convert_to_olap(const UInt8* null_map, const ColumnString* column_array);
        Status convert_to_olap() override;

    private:
        bool _check_length;
        bool _is_jsonb =
                false; // Make sure that the json binary data written in is the correct jsonb value.
        PaddedPODArray<Slice> _slice;
    };

    class OlapColumnDataConvertorAggState : public OlapColumnDataConvertorBase {
    public:
        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        const void* get_data() const override;
        const void* get_data_at(size_t offset) const override {
            throw doris::Exception(ErrorCode::NOT_IMPLEMENTED_ERROR,
                                   "OlapColumnDataConvertorAggState not support get_data_at");
        }
        Status convert_to_olap() override;

    private:
        PaddedPODArray<Slice> _slice;
    };

    template <typename T>
    class OlapColumnDataConvertorPaddedPODArray : public OlapColumnDataConvertorBase {
    public:
        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override {
            OlapColumnDataConvertorBase::set_source_column(typed_column, row_pos, num_rows);
            _values.resize(num_rows);
        }
        const void* get_data() const override { return _values.data(); }
        const void* get_data_at(size_t offset) const override {
            UInt8 null_flag = 0;
            if (get_nullmap()) {
                null_flag = get_nullmap()[offset];
            }
            return null_flag ? nullptr : _values.data() + offset;
        }

    protected:
        PaddedPODArray<T> _values;
    };

    class OlapColumnDataConvertorDate : public OlapColumnDataConvertorPaddedPODArray<uint24_t> {
    public:
        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        Status convert_to_olap() override;
    };

    class OlapColumnDataConvertorDateTime : public OlapColumnDataConvertorPaddedPODArray<uint64_t> {
    public:
        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        Status convert_to_olap() override;
    };

    class OlapColumnDataConvertorDecimal
            : public OlapColumnDataConvertorPaddedPODArray<decimal12_t> {
    public:
        Status convert_to_olap() override;
    };

    // class OlapColumnDataConvertorSimple for simple types, which don't need to do any convert, like int, float, double, etc...
    template <PrimitiveType T>
    class OlapColumnDataConvertorSimple : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorSimple() = default;
        ~OlapColumnDataConvertorSimple() override = default;

        const void* get_data() const override { return _values; }

        const void* get_data_at(size_t offset) const override {
            assert(offset < _num_rows);
            UInt8 null_flag = 0;
            if (get_nullmap()) {
                null_flag = get_nullmap()[offset];
            }
            return null_flag ? nullptr : _values + offset;
        }

        Status convert_to_olap() override {
            const typename PrimitiveTypeTraits<T>::ColumnType* column_data = nullptr;
            if (_nullmap) {
                auto nullable_column =
                        assert_cast<const vectorized::ColumnNullable*>(_typed_column.column.get());
                column_data = assert_cast<const typename PrimitiveTypeTraits<T>::ColumnType*>(
                        nullable_column->get_nested_column_ptr().get());
            } else {
                column_data = assert_cast<const typename PrimitiveTypeTraits<T>::ColumnType*>(
                        _typed_column.column.get());
            }

            assert(column_data);
            _values =
                    (const typename PrimitiveTypeTraits<T>::ColumnItemType*)(column_data->get_data()
                                                                                     .data()) +
                    _row_pos;
            return Status::OK();
        }

    protected:
        const typename PrimitiveTypeTraits<T>::ColumnItemType* _values = nullptr;
    };

    class OlapColumnDataConvertorDateV2 : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorDateV2() = default;
        ~OlapColumnDataConvertorDateV2() override = default;

        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override {
            OlapColumnDataConvertorBase::set_source_column(typed_column, row_pos, num_rows);
        }

        const void* get_data() const override { return values_; }

        const void* get_data_at(size_t offset) const override {
            assert(offset < _num_rows);
            UInt8 null_flag = 0;
            if (get_nullmap()) {
                null_flag = get_nullmap()[offset];
            }
            return null_flag ? nullptr : values_ + offset;
        }

        Status convert_to_olap() override {
            const vectorized::ColumnDateV2* column_data = nullptr;
            if (_nullmap) {
                auto nullable_column =
                        assert_cast<const vectorized::ColumnNullable*>(_typed_column.column.get());
                column_data = assert_cast<const vectorized::ColumnDateV2*>(
                        nullable_column->get_nested_column_ptr().get());
            } else {
                column_data =
                        assert_cast<const vectorized::ColumnDateV2*>(_typed_column.column.get());
            }

            assert(column_data);
            values_ = (const uint32_t*)(column_data->get_data().data()) + _row_pos;
            return Status::OK();
        }

    private:
        const uint32_t* values_ = nullptr;
    };

    class OlapColumnDataConvertorDateTimeV2 : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorDateTimeV2() = default;
        ~OlapColumnDataConvertorDateTimeV2() override = default;

        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override {
            OlapColumnDataConvertorBase::set_source_column(typed_column, row_pos, num_rows);
        }

        const void* get_data() const override { return values_; }

        const void* get_data_at(size_t offset) const override {
            assert(offset < _num_rows);
            UInt8 null_flag = 0;
            if (get_nullmap()) {
                null_flag = get_nullmap()[offset];
            }
            return null_flag ? nullptr : values_ + offset;
        }

        Status convert_to_olap() override {
            const vectorized::ColumnDateTimeV2* column_data = nullptr;
            if (_nullmap) {
                auto nullable_column =
                        assert_cast<const vectorized::ColumnNullable*>(_typed_column.column.get());
                column_data = assert_cast<const vectorized::ColumnDateTimeV2*>(
                        nullable_column->get_nested_column_ptr().get());
            } else {
                column_data = assert_cast<const vectorized::ColumnDateTimeV2*>(
                        _typed_column.column.get());
            }

            assert(column_data);
            values_ = (const uint64_t*)(column_data->get_data().data()) + _row_pos;
            return Status::OK();
        }

    private:
        const uint64_t* values_ = nullptr;
    };

    // decimalv3 don't need to do any convert
    template <PrimitiveType T>
    class OlapColumnDataConvertorDecimalV3 : public OlapColumnDataConvertorSimple<T> {
    public:
        OlapColumnDataConvertorDecimalV3() = default;
        ~OlapColumnDataConvertorDecimalV3() override = default;

        Status convert_to_olap() override {
            using ColumnType = typename PrimitiveTypeTraits<T>::ColumnType;
            const ColumnType* column_data = nullptr;
            if (this->_nullmap) {
                auto nullable_column = assert_cast<const vectorized::ColumnNullable*>(
                        this->_typed_column.column.get());
                column_data = assert_cast<const ColumnType*>(
                        nullable_column->get_nested_column_ptr().get());
            } else {
                column_data = assert_cast<const ColumnType*>(this->_typed_column.column.get());
            }

            assert(column_data);
            this->_values =
                    (const typename PrimitiveTypeTraits<T>::ColumnItemType*)(column_data->get_data()
                                                                                     .data()) +
                    this->_row_pos;
            return Status::OK();
        }
    };

    class OlapColumnDataConvertorStruct : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorStruct(
                std::vector<OlapColumnDataConvertorBaseUPtr>& sub_convertors) {
            for (auto& sub_convertor : sub_convertors) {
                _sub_convertors.push_back(std::move(sub_convertor));
            }
            size_t allocate_size = _sub_convertors.size() * 2;
            _results.resize(allocate_size);
        }
        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        const void* get_data() const override;
        const void* get_data_at(size_t offset) const override {
            throw doris::Exception(ErrorCode::NOT_IMPLEMENTED_ERROR,
                                   "OlapColumnDataConvertorStruct not support get_data_at");
        }
        Status convert_to_olap() override;

    private:
        std::vector<OlapColumnDataConvertorBaseUPtr> _sub_convertors;
        std::vector<const void*> _results;
    };

    class OlapColumnDataConvertorArray : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorArray(OlapColumnDataConvertorBaseUPtr item_convertor,
                                     const TabletColumn& column)
                : _item_convertor(std::move(item_convertor)),
                  _data_type(DataTypeFactory::instance().create_data_type(column)) {
            _base_offset = 0;
            _results.resize(4); // size + offset + item_data + item_nullmap
        }

        const void* get_data() const override { return _results.data(); };
        const void* get_data_at(size_t offset) const override {
            throw doris::Exception(ErrorCode::NOT_IMPLEMENTED_ERROR,
                                   "OlapColumnDataConvertorArray not support get_data_at");
        }
        Status convert_to_olap() override;

    private:
        Status convert_to_olap(const ColumnArray* column_array);
        OlapColumnDataConvertorBaseUPtr _item_convertor;
        UInt64 _base_offset;
        PaddedPODArray<UInt64> _offsets; // array offsets in disk layout
        // size + offsets_data + item_data + item_nullmap
        std::vector<const void*> _results;
        DataTypeArray _data_type;
    };

    class OlapColumnDataConvertorMap : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorMap(const TabletColumn& key_column, const TabletColumn& value_column)
                : _key_convertor(create_olap_column_data_convertor(key_column)),
                  _value_convertor(create_olap_column_data_convertor(value_column)),
                  _data_type(DataTypeFactory::instance().create_data_type(key_column),
                             DataTypeFactory::instance().create_data_type(value_column)) {
            _base_offset = 0;
            _results.resize(6); // size + offset + k_data + v_data +  k_nullmap + v_nullmap
        }

        Status convert_to_olap() override;
        const void* get_data() const override { return _results.data(); };
        const void* get_data_at(size_t offset) const override {
            throw doris::Exception(ErrorCode::NOT_IMPLEMENTED_ERROR,
                                   "OlapColumnDataConvertorMap not support get_data_at");
        }

    private:
        Status convert_to_olap(const ColumnMap* column_map);
        OlapColumnDataConvertorBaseUPtr _key_convertor;
        OlapColumnDataConvertorBaseUPtr _value_convertor;
        std::vector<const void*> _results;
        PaddedPODArray<UInt64> _offsets; // map offsets in disk layout
        UInt64 _base_offset;
        DataTypeMap _data_type;
    }; //OlapColumnDataConvertorMap

    class OlapColumnDataConvertorVariant : public OlapColumnDataConvertorBase {
    public:
        OlapColumnDataConvertorVariant() = default;

        void set_source_column(const ColumnWithTypeAndName& typed_column, size_t row_pos,
                               size_t num_rows) override;
        Status convert_to_olap() override;

        const void* get_data() const override;
        const void* get_data_at(size_t offset) const override {
            throw doris::Exception(ErrorCode::NOT_IMPLEMENTED_ERROR,
                                   "OlapColumnDataConvertorVariant not support get_data_at");
        }

    private:
        // // encodes sparsed columns
        // const ColumnString* _root_data_column;
        // // _nullmap contains null info for this variant
        std::unique_ptr<OlapColumnDataConvertorVarChar> _root_data_convertor;
        ColumnVariant* _source_column_ptr;
    };

private:
    std::vector<OlapColumnDataConvertorBaseUPtr> _convertors;
};

} // namespace vectorized
} // namespace doris
