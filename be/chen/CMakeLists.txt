add_executable(vwal_test vwal_scanner_main_test.cpp)
target_link_libraries(vwal_test PRIVATE ${DORIS_LINK_LIBS})

add_executable(block_test block_test.cpp)
target_link_libraries(block_test PRIVATE ${DORIS_LINK_LIBS})

# NOTE: should define BE_TEST
# add_executable(test_load_stream ${CMAKE_CURRENT_SOURCE_DIR}/../test/runtime/load_stream_test.cpp)
# target_link_libraries(test_load_stream ${TEST_LINK_LIBS})
