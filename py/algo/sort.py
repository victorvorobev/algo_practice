"""
Sorting algorithms
"""


def bubble_sort(array: list[int]) -> list[int]:
    """
    Simplest sorting algorithm O(n^2)
    :param array: Array to sort
    :return: Sorted array
    """
    array_size = len(array)
    if array_size <= 1:
        return array

    for i in range(array_size):
        swapped = False
        for j in range(array_size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array
