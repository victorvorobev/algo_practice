"""
Tests for search functions
"""

import random

import pytest
from algo import search

MAX_VALUE = 1_000_000

TEST_DATA = [
    pytest.param(random.sample(range(-1 * MAX_VALUE, MAX_VALUE), 100), id='small_even_len'),
    pytest.param(random.sample(range(-1 * MAX_VALUE, MAX_VALUE), 101), id='small_odd_len'),
    pytest.param(random.sample(range(-1 * MAX_VALUE, MAX_VALUE), 1_000_000), id='big_even_len'),
    pytest.param(random.sample(range(-1 * MAX_VALUE, MAX_VALUE), 1_000_001), id='big_odd_len'),
]

SEARCH_FUNCTIONS = [
    search.linear_search
]


@pytest.fixture(name='should_be_found', params=[True, False], ids=['should_found', 'should_not_found'])
def should_be_found_fixture(request):
    """Fixture flag that shows whether target value should be found in test data array or not"""
    return request.param


@pytest.fixture(name='should_be_sorted', params=[True, False], ids=['should_be_sorted', 'should_not_be_sorted'])
def should_be_sorted_fixture(request):
    """Fixture flag that shows whether test data array should be sorted or not"""
    return request.param


@pytest.fixture(name='test_data')
def test_data_fixture(should_be_found, should_be_sorted, request):
    """
    Fixture that prepares test data
    :param should_be_found: flag that shows whether returned target value should be findable or not
    :param should_be_sorted: flag that shows whether returned array should be sorted or not
    :param request: request that contains test array as a parameter
    :return: array to search in, target value to search, expected result
    """
    data = request.param
    if should_be_sorted:
        data.sort()
    if should_be_found:
        expected_result = random.randint(0, len(data) - 1)
        target_value = data[expected_result]
    else:
        expected_result = None
        while True:
            target_value = data[random.randint(0, len(data) - 1)]
            target_value -= 1
            if target_value not in data:
                break
    return request.param, target_value, expected_result


@pytest.mark.parametrize('test_data', TEST_DATA, indirect=True)
@pytest.mark.parametrize('search_func', SEARCH_FUNCTIONS)
def test_search(test_data, search_func):
    """Test function that covers all cases with search algorithms"""
    data, target_value, expected_result = test_data
    assert expected_result == search_func(data, target_value)
