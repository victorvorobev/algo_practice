"""
Tests for search functions
"""
import random
from dataclasses import dataclass

import pytest
from algo import search

MAX_VALUE = 1_000_000


@dataclass
class FuncToTest:
    """
    Data class to hold test function with some test parameters
    """
    func: callable
    sort_required: bool


SEARCH_FUNCTIONS = [
    pytest.param(FuncToTest(func=search.linear_search, sort_required=False), id='linear_search'),
    pytest.param(FuncToTest(func=search.binary_search, sort_required=True), id='binary_search'),
]


@pytest.fixture(name='search_func', params=SEARCH_FUNCTIONS)
def search_func_fixture(request):
    """Fixture that returns test function with its meta information"""
    return request.param


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
def test_data_fixture(should_be_found, should_be_sorted, data_sample, search_func):
    """
    Fixture that prepares test data
    :param should_be_found: flag that shows whether returned target value should be findable or not
    :param should_be_sorted: flag that shows whether returned array should be sorted or not
    :param data_sample: fixture test array as a parameter
    :return: array to search in, target value to search, expected result
    """
    if not should_be_sorted and search_func.sort_required:
        pytest.skip('Skip test due to unsorted input and required sorted data')

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
    return search_func.func, data_sample, target_value, expected_result


def test_search(test_data):
    """Test function that covers all cases with search algorithms"""
    search_func, data, target_value, expected_result = test_data
    assert expected_result == search_func(data, target_value)
