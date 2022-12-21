"""
Search algorithms
"""


def linear_search(array: list[int], target: int) -> int | None:
    """
    The simplest search algorithm. O(n)
    :param array: Array to search in
    :param target: Target element to find
    :return: index of found element or None
    """
    for i, element in enumerate(array):
        if element == target:
            return i
    return None


def binary_search(array: list[int], target: int) -> int | None:
    """
    Divide and check again. O(log(n))
    :param array: Array to search in
    :param target: Target element to find
    :return: index of found element or None
    """
    start, end = 0, len(array) - 1
    while start <= end:
        check_index = (start + end) // 2
        check_value = array[check_index]
        if check_value == target:
            return check_index
        if check_value < target:
            start = check_index + 1
        else:
            end = check_index - 1
    return None


def binary_search_recursive(array: list[int], target: int) -> int | None:
    """
    Divide and check again, but recursively O(log(n))
    :param array: Array to search in
    :param target: Target element to find
    :return: index of found element or None
    """

    def search(_array, _target, _start, _end):
        check_index = (_start + _end) // 2
        check_value = array[check_index]
        if _start > _end:
            return None
        if check_value == target:
            return check_index
        if check_value < target:
            return search(_array, _target, check_index + 1, _end)
        return search(_array, _target, _start, check_index - 1)

    return search(array, target, 0, len(array) - 1)
