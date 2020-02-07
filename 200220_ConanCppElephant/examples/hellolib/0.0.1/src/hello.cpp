#include "hellolib/hello.h"

#include <string>
#include <iostream>


void hello() {

    #ifdef NDEBUG
    const std::string build_type = "Release";
    #else
    const std::string build_type = "Debug";
    #endif

    std::cout << "Hello " << build_type << " world!" << std::endl;
}