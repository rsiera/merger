from array import array
from unittest import TestCase

from merger import merge_sorted_arrays


class MergerTest(TestCase):
    def test_should_return_empty_when_empty_arrays(self):
        first_array = array('l')
        second_array = array('l')
        merged_array = merge_sorted_arrays(first_array, second_array)
        self.assertEqual(array('l'), merged_array)

    def test_should_return_second_array_when_first_empty(self):
        first_array = array('l')
        second_array = array('l', [1, 2, 3])
        merged_array = merge_sorted_arrays(first_array, second_array)
        self.assertEqual(array('l', [1, 2, 3]), merged_array)

    def test_should_return_first_array_when_second_empty(self):
        first_array = array('l', [2, 3, 4])
        second_array = array('l')
        merged_array = merge_sorted_arrays(first_array, second_array)
        self.assertEqual(array('l', [2, 3, 4]), merged_array)

    def test_should_return_merged_sorted_array_when_first_second_equal_len(self):
        first_array = array('l', [2, 3, 4])
        second_array = array('l', [3, 4, 5])
        merged_array = merge_sorted_arrays(first_array, second_array)
        self.assertEqual(array('l', [2, 3, 3, 4, 4, 5]), merged_array)

    def test_should_return_merged_sorted_array_when_first_bigger_than_second(self):
        first_array = array('l', [2, 3, 4, 5, 10, 29])
        second_array = array('l', [3, 4, 5])
        merged_array = merge_sorted_arrays(first_array, second_array)
        self.assertEqual(array('l', [2, 3, 3, 4, 4, 5, 5, 10, 29]), merged_array)

    def test_should_return_merged_sorted_array_when_second_bigger_than_first(self):
        first_array = array('l', [2, 3])
        second_array = array('l', [3, 4, 7, 29])
        merged_array = merge_sorted_arrays(first_array, second_array)
        self.assertEqual(array('l', [2, 3, 3, 4, 7, 29]), merged_array)
