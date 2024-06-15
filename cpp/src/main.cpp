#include <vector>
#include <iostream>

#include "search.h"

int main()
{
    std::vector<int> data = {10, 20, 30, 40};
    int key = 30;
    int result = linearSearch(data, key);
    if (result != -1)
    {
        std::cout << "Found at index: " << result << std::endl;
    }
    else
    {
        std::cout << "Failed to find element" << std::endl;
    }
}
