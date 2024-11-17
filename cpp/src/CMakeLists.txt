add_library(${PROJECT_NAME} STATIC dummy.cpp)

# include public headers
target_include_directories(${PROJECT_NAME}
    PUBLIC "${PROJECT_BINARY_DIR}" include
)

if(BUILD_AP_TESTS)
    add_subdirectory(tests)
endif(BUILD_AP_TESTS)
