add_executable(vwal_test vwal_scanner_main_test.cpp)
target_link_libraries(vwal_test PRIVATE ${DORIS_LINK_LIBS})

add_executable(block_test block_test.cpp)
target_link_libraries(block_test PRIVATE ${DORIS_LINK_LIBS})
