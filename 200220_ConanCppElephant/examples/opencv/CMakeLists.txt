cmake_minimum_required(VERSION 2.8.12)

project(CameraApp CXX)

set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})
set(CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR} ${CMAKE_PREFIX_PATH})

find_package(opencv)

add_executable(camera main.cpp)
target_link_libraries(camera opencv::opencv)
set_target_properties(camera PROPERTIES RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_BINARY_DIR}/bin")