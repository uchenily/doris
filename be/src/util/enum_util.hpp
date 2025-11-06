#pragma once

#include <array>
#include <string>
#include <string_view>
#include <type_traits>
#include <utility>

namespace util {
namespace detail {

template <auto Value>
constexpr auto enum_name() {
#if defined(__GNUC__) || defined(__clang__)
    // auto enum_name() [with auto Value = xxx::yyy::zzz]
    auto func_name = std::string_view {__PRETTY_FUNCTION__};
    auto start = func_name.find('=') + 2;
    auto end = func_name.size() - 1;
#else
    static_assert(false, "Unsupported compiler");
#endif

    auto name = std::string_view {func_name.data() + start, end - start};
    auto pos = name.rfind("::");
    if (start != std::string_view::npos) {
        pos += 2;
        name = std::string_view {name.data() + pos, name.size() - pos};
    }
    return name.find(')') == std::string_view::npos ? name : "";
}

template <typename T, size_t... N>
constexpr auto generate_enum_names(std::index_sequence<N...> /*seq*/) {
    return std::array<std::string_view, sizeof...(N)> {enum_name<static_cast<T>(N)>()...};
}

template <typename T, size_t N = 0>
constexpr auto enum_max() {
    if constexpr (!enum_name<static_cast<T>(N)>().empty()) {
        return enum_max<T, N + 1>();
    } else {
        return N;
    }
}
} // namespace detail

// NOTE: only enum types without custom values are supported
template <typename T>
auto EnumName(const T& value) -> std::string
    requires(std::is_enum_v<T>)
{
    constexpr auto N = detail::enum_max<T>();
    constexpr auto names = detail::generate_enum_names<T>(std::make_index_sequence<N> {});
    return std::string {names[static_cast<size_t>(value)]};
}

template <typename T>
constexpr auto EnumType(std::string_view name) -> T
    requires(std::is_enum_v<T>)
{
    constexpr auto N = detail::enum_max<T>();
    constexpr auto names = detail::generate_enum_names<T>(std::make_index_sequence<N> {});
    for (auto i = 0U; i < names.size(); i++) {
        if (names[i] == name) {
            return static_cast<T>(i);
        }
    }
    // static_assert(false, "Unknown enum type name");
    return static_cast<T>(0);
}
} // namespace util
