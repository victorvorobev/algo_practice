"""
Tests for sort functions
"""

import random

import pytest
from algo import sort

MAX_VALUE = 1_000_000

SORT_FUNCTIONS = [
    pytest.param(sort.bubble_sort, id="bubble_sort"),
    pytest.param(sort.merge_sort, id="merge_sort"),
    pytest.param(sort.quick_sort, id="quick_sort"),
    pytest.param(sort.select_sort, id="select_sort"),
]


@pytest.fixture(name="sort_func", params=SORT_FUNCTIONS)
def sort_func_fixture(request):
    """Fixture that returns test function with its meta information"""
    return request.param


SAMPLE_LENS = [
    0,
    1,
    2,
    3,
    4,
    10,
    11,
]


@pytest.fixture(
    name="data_sample", params=SAMPLE_LENS, ids=[f"len_{i}" for i in SAMPLE_LENS]
)
def data_sample_fixture(request):
    """Fixture that generates array to sort"""
    if not request.param:
        return []
    return list(random.sample(range(-1 * MAX_VALUE, MAX_VALUE), request.param))


@pytest.fixture(name="test_data")
def test_data_fixture(data_sample, sort_func):
    """
    Fixture that prepares test data
    :param data_sample: fixture test array as a parameter
    :return: sort function, array to sort, expected result
    """
    expected_result = sorted(data_sample)
    return sort_func, data_sample, expected_result


def test_search(test_data):
    """Test function that covers all cases with sort algorithms"""
    sort_func, data, expected_result = test_data
    print(f"{data = }")
    result = sort_func(data)
    print(f"{result = }")
    assert expected_result == result
