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
// This file is copied from
// https://github.com/ClickHouse/ClickHouse/blob/master/src/Functions/registerFunctions.h
// and modified by Doris

#pragma once

#include <mutex>
#include <string>

#include "vec/functions/function.h"

namespace doris::vectorized {

constexpr auto DECIMAL256_FUNCTION_SUFFIX {"_decimal256"};

class SimpleFunctionFactory;

void register_function_plus(SimpleFunctionFactory& factory);
void register_function_minus(SimpleFunctionFactory& factory);
void register_function_comparison_greater(SimpleFunctionFactory& factory);

class SimpleFunctionFactory {
    using Creator = std::function<FunctionBuilderPtr()>;
    using FunctionCreators = phmap::flat_hash_map<std::string, Creator>;
    using FunctionIsVariadic = phmap::flat_hash_set<std::string>;
    /// @TEMPORARY: for be_exec_version=5.
    /// whenever change this, please make sure old functions was all cleared. otherwise the version now-1 will think it should do replacement
    /// which actually should be done by now-2 version.
    constexpr static int NEWEST_VERSION_FUNCTION_SUBSTITUTE = 5;

    /// @TEMPORARY: for be_exec_version=8.
    constexpr static int NEWEST_VERSION_EXPLODE_MULTI_PARAM = 8;

public:
    void register_function(const std::string& name, const Creator& ptr) {
        //TODO: should add check of is_variadic. or just remove is_variadic is ok?
        DataTypes types = ptr()->get_variadic_argument_types();
        // types.empty() means function is not variadic
        if (!types.empty()) {
            function_variadic_set.insert(name);
        }
        std::string key_str = name;
        if (!types.empty()) {
            for (const auto& type : types) {
                key_str.append(type->get_family_name());
            }
        }
        function_creators[key_str] = ptr;
    }

    template <class Function>
    void register_function() {
        if constexpr (std::is_base_of_v<IFunction, Function>) {
            register_function(Function::name, &createDefaultFunction<Function>);
        } else {
            register_function(Function::name, &Function::create);
        }
    }

    template <class Function>
    void register_function(std::string name) {
        register_function(name, &createDefaultFunction<Function>);
    }

    /// @TEMPORARY: for be_exec_version=8
    template <class Function>
    void register_alternative_function(std::string name) {
        static std::string suffix {"_old"};
        function_to_replace[name] = name + suffix;
        register_function(name + suffix, &createDefaultFunction<Function>);
    }

    void register_alias(const std::string& name, const std::string& alias) {
        function_alias[alias] = name;
    }

    FunctionBasePtr get_function(const std::string& name, const ColumnsWithTypeAndName& arguments,
                                 const DataTypePtr& return_type, const FunctionAttr& attr = {},
                                 int be_version = 0) {
        std::string key_str = name;

        if (function_alias.contains(name)) {
            key_str = function_alias[name];
        }

        if (attr.enable_decimal256) {
            if (key_str == "array_sum" || key_str == "array_avg" || key_str == "array_product" ||
                key_str == "array_cum_sum") {
                key_str += DECIMAL256_FUNCTION_SUFFIX;
            }
        }

        if ((key_str.starts_with("unix_timestamp") || key_str.starts_with("from_unixtime")) &&
            attr.new_version_unix_timestamp) {
            key_str += "_new";
        }

        temporary_function_update(be_version, key_str);

        // if function is variadic, added types_str as key
        if (function_variadic_set.count(key_str)) {
            for (const auto& arg : arguments) {
                key_str.append(arg.type->is_nullable()
                                       ? reinterpret_cast<const DataTypeNullable*>(arg.type.get())
                                                 ->get_nested_type()
                                                 ->get_family_name()
                                       : arg.type->get_family_name());
            }
        }

        auto iter = function_creators.find(key_str);
        if (iter == function_creators.end()) {
            // use original name as signature without variadic arguments
            iter = function_creators.find(name);
            if (iter == function_creators.end()) {
                LOG(WARNING) << fmt::format("Function signature {} is not found", key_str);
                return nullptr;
            }
        }

        return iter->second()->build(arguments, return_type);
    }

private:
    FunctionCreators function_creators;
    FunctionIsVariadic function_variadic_set;
    std::unordered_map<std::string, std::string> function_alias;
    /// @TEMPORARY: for be_exec_version=8. replace function to old version.
    std::unordered_map<std::string, std::string> function_to_replace;

    template <typename Function>
    static FunctionBuilderPtr createDefaultFunction() {
        return std::make_shared<DefaultFunctionBuilder>(Function::create());
    }

    /// @TEMPORARY: for be_exec_version=8
    void temporary_function_update(int fe_version_now, std::string& name) {
        // replace if fe is old version.
        if (fe_version_now < NEWEST_VERSION_EXPLODE_MULTI_PARAM &&
            function_to_replace.contains(name)) {
            name = function_to_replace[name];
        }
    }

public:
    static SimpleFunctionFactory& instance() {
        static std::once_flag oc;
        static SimpleFunctionFactory instance;
        std::call_once(oc, []() {
            register_function_plus(instance);
            register_function_minus(instance);
            register_function_comparison_greater(instance);
        });
        return instance;
    }
};
} // namespace doris::vectorized
