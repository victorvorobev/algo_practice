cmake_minimum_required(VERSION 3.14)

project(algo_practice VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(BUILD_AP_TESTS "Build tests" ON)

message(STATUS "==================== algo-practice ====================")
message(STATUS "Build algo practice tests: ${BUILD_AP_TESTS}")
message(STATUS "=======================================================")

add_subdirectory(src)
