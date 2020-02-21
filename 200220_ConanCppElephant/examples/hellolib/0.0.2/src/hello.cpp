#include "hellolib/hello.h"

#include <fmt/format.h>
#include "fmt/printf.h"
#include "fmt/ostream.h"
#include "fmt/color.h"


void hello() {

    #ifdef NDEBUG
    const std::string build_type = "Release";
    #else
    const std::string build_type = "Debug";
    #endif

    std::string message = fmt::format(fmt::emphasis::bold | fg(fmt::color::red),
                                      "Hello {} world!", build_type);

    fmt::print(message);
}