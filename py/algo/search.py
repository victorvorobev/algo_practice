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
