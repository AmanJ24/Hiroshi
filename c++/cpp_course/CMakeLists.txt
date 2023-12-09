cmake_minimum_required(VERSION 3.28.0)
project(main VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

add_executable(main functions.cpp)

set(CPACK_PROJECT_NAME main)
set(CPACK_PROJECT_VERSION 0.1)
include(CPack)
