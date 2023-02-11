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


def merge_sort(array: list[int]) -> list[int]:
    """
    Divide and conquer, O(nlog(n))
    :param array: Array to sort
    :return: sorted array
    """
    array_size = len(array)
    if array_size <= 1:
        return array

    mid = array_size // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    result = []
    l_index = r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    while l_index < len(left):
        result.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        result.append(right[r_index])
        r_index += 1

    return result
