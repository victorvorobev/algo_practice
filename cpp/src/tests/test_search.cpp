#include <gtest/gtest.h>

#include "my_search.h"

#include <iostream>
#include <vector>

TEST(TestSearch, LiniarSearchFound) {
  std::vector<int> data = {10, 20, 30, 40};
  int key = 30;
  int result = linearSearch(data, key);
  EXPECT_EQ(result, 2);
}

TEST(TestSearch, LiniarSearchNotFound) {
  std::vector<int> data = {10, 20, 30, 40};
  int key = 5;
  int result = linearSearch(data, key);
  EXPECT_EQ(result, -1);
}
