"""
Tests for search functions
"""

import random

import pytest
from algo import search

MAX_VALUE = 1_000_000

SEARCH_FUNCTIONS = [
    search.linear_search,
]


@pytest.fixture(name='data_sample',
                params=[10, 11, 1_000_000, 1_000_001],
                ids=['small_even_len', 'small_odd_len', 'big_even_len', 'big_odd_len'])
def data_sample_fixture(request):
    """Fixture that generates data sample"""
    return list(random.sample(range(-1 * MAX_VALUE, MAX_VALUE), request.param))


@pytest.fixture(name='should_be_found', params=[True, False], ids=['should_found', 'should_not_found'])
def should_be_found_fixture(request):
    """Fixture flag that shows whether target value should be found in test data array or not"""
    return request.param


@pytest.fixture(name='should_be_sorted', params=[True, False], ids=['should_be_sorted', 'should_not_be_sorted'])
def should_be_sorted_fixture(request):
    """Fixture flag that shows whether test data array should be sorted or not"""
    return request.param


@pytest.fixture(name='test_data')
def test_data_fixture(should_be_found, should_be_sorted, data_sample):
    """
    Fixture that prepares test data
    :param should_be_found: flag that shows whether returned target value should be findable or not
    :param should_be_sorted: flag that shows whether returned array should be sorted or not
    :param data_sample: fixture test array as a parameter
    :return: array to search in, target value to search, expected result
    """

    if should_be_sorted:
        data_sample.sort()
    if should_be_found:
        expected_result = random.randint(0, len(data_sample) - 1)
        target_value = data_sample[expected_result]
    else:
        expected_result = None
        while True:
            target_value = data_sample[random.randint(0, len(data_sample) - 1)]
            target_value -= 1
            if target_value not in data_sample:
                break
    return data_sample, target_value, expected_result


@pytest.mark.parametrize('search_func', SEARCH_FUNCTIONS)
def test_search(test_data, search_func):
    """Test function that covers all cases with search algorithms"""
    data, target_value, expected_result = test_data
    assert expected_result == search_func(data, target_value)
