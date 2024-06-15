#include <vector>

template <typename T>
int linearSearch(std::vector<T> &list, T target)
{
    for (int i = 0; i < list.size(); i++)
    {
        if (list[i] == target)
        {
            return i;
        }
    }

    return -1;
}
