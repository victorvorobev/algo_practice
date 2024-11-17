if(BUILD_AP_TESTS)
    message(STATUS "Building test dependencies")
    # enabled testing
    enable_testing()

    # fetch googletest
    include(FetchContent)
    FetchContent_Declare(
        googletest
        GIT_REPOSITORY https://github.com/google/googletest.git
        GIT_TAG v1.15.2
    )
    # For Windows: Prevent overriding the parent project's compiler/linker settings

    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)

    add_executable(tests
        my_test.cpp 
        test_search.cpp
    )

    target_link_libraries(tests
        algo_practice
        GTest::gtest_main
    )
    include(GoogleTest)
    gtest_discover_tests(tests)
    
endif(BUILD_AP_TESTS)
