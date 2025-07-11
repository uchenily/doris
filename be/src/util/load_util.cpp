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

#include "util/load_util.h"

#include <string>

#include "util/string_util.h"

namespace doris {
void LoadUtil::parse_format(const std::string& format_str, const std::string& compress_type_str,
                            TFileFormatType::type* format_type,
                            TFileCompressType::type* compress_type) {
    if (format_str.empty()) {
        parse_format("CSV", compress_type_str, format_type, compress_type);
        return;
    }

    // Assign compress_type
    if (iequal(compress_type_str, "GZ")) {
        *compress_type = TFileCompressType::GZ;
    } else if (iequal(compress_type_str, "LZO")) {
        *compress_type = TFileCompressType::LZO;
    } else if (iequal(compress_type_str, "BZ2")) {
        *compress_type = TFileCompressType::BZ2;
    } else if (iequal(compress_type_str, "LZ4")) {
        *compress_type = TFileCompressType::LZ4FRAME;
    } else if (iequal(compress_type_str, "LZ4_BLOCK")) {
        *compress_type = TFileCompressType::LZ4BLOCK;
    } else if (iequal(compress_type_str, "LZOP")) {
        *compress_type = TFileCompressType::LZO;
    } else if (iequal(compress_type_str, "SNAPPY_BLOCK")) {
        *compress_type = TFileCompressType::SNAPPYBLOCK;
    } else if (iequal(compress_type_str, "DEFLATE")) {
        *compress_type = TFileCompressType::DEFLATE;
    } else {
        *compress_type = TFileCompressType::PLAIN;
    }

    // Assign format_type
    *format_type = TFileFormatType::FORMAT_UNKNOWN;
    if (iequal(format_str, "CSV")) {
        if (compress_type_str.empty()) {
            *format_type = TFileFormatType::FORMAT_CSV_PLAIN;
        } else if (iequal(compress_type_str, "GZ")) {
            *format_type = TFileFormatType::FORMAT_CSV_GZ;
        } else if (iequal(compress_type_str, "LZO")) {
            *format_type = TFileFormatType::FORMAT_CSV_LZO;
        } else if (iequal(compress_type_str, "BZ2")) {
            *format_type = TFileFormatType::FORMAT_CSV_BZ2;
        } else if (iequal(compress_type_str, "LZ4")) {
            *format_type = TFileFormatType::FORMAT_CSV_LZ4FRAME;
        } else if (iequal(compress_type_str, "LZ4_BLOCK")) {
            *format_type = TFileFormatType::FORMAT_CSV_LZ4BLOCK;
        } else if (iequal(compress_type_str, "LZOP")) {
            *format_type = TFileFormatType::FORMAT_CSV_LZOP;
        } else if (iequal(compress_type_str, "SNAPPY_BLOCK")) {
            *format_type = TFileFormatType::FORMAT_CSV_SNAPPYBLOCK;
        } else if (iequal(compress_type_str, "DEFLATE")) {
            *format_type = TFileFormatType::FORMAT_CSV_DEFLATE;
        }
    } else if (iequal(format_str, "HIVE_TEXT")) {
        *format_type = TFileFormatType::FORMAT_TEXT;
    } else if (iequal(format_str, "JSON")) {
        *format_type = TFileFormatType::FORMAT_JSON;
    } else if (iequal(format_str, "PARQUET")) {
        *format_type = TFileFormatType::FORMAT_PARQUET;
    } else if (iequal(format_str, "ORC")) {
        *format_type = TFileFormatType::FORMAT_ORC;
    } else if (iequal(format_str, "WAL")) {
        *format_type = TFileFormatType::FORMAT_WAL;
    } else if (iequal(format_str, "ARROW")) {
        *format_type = TFileFormatType::FORMAT_ARROW;
    }
}

bool LoadUtil::is_format_support_streaming(TFileFormatType::type format) {
    switch (format) {
    case TFileFormatType::FORMAT_CSV_PLAIN:
    case TFileFormatType::FORMAT_CSV_BZ2:
    case TFileFormatType::FORMAT_CSV_DEFLATE:
    case TFileFormatType::FORMAT_CSV_GZ:
    case TFileFormatType::FORMAT_CSV_LZ4FRAME:
    case TFileFormatType::FORMAT_CSV_LZ4BLOCK:
    case TFileFormatType::FORMAT_CSV_LZO:
    case TFileFormatType::FORMAT_CSV_LZOP:
    case TFileFormatType::FORMAT_JSON:
    case TFileFormatType::FORMAT_TEXT:
    case TFileFormatType::FORMAT_WAL:
    case TFileFormatType::FORMAT_ARROW:
        return true;
    default:
        return false;
    }
}
} // namespace  doris
