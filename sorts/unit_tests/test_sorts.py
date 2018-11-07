import unittest
from assertpy import assert_that
from sorts.bubble_sort import bubblesort
from sorts.heap_sort import heapsort
from sorts.insertion_sort import insertionsort
from sorts.merge_sort import mergesort
from sorts.quick_sort import quicksort
from sorts.radix_sort import radixsort
from sorts.selection_sort import selectionsort

class TestSorts(unittest.TestCase):
    def setUp(self):
        # test arr
        self.unsorted = [10, 9, 8, 7, 6, 2, 4, 5]
        self.sorted = [2, 4, 5, 6, 7, 8, 9, 10]

    def test_bubble_sort(self):
        _sorted = bubblesort(self.unsorted)
        assert_that(_sorted).is_equal_to(self.sorted)

    def test_heap_sort(self):
        _sorted = heapsort(self.unsorted)
        assert_that(_sorted).is_equal_to(self.sorted)

    def test_insertion_sort(self):
        _sorted = insertionsort(self.unsorted)
        assert_that(_sorted).is_equal_to(self.sorted)

    def test_merge_sort(self):
        _sorted = mergesort(self.unsorted)
        assert_that(_sorted).is_equal_to(self.sorted)

    def test_quick_sort(self):
        _sorted = quicksort(self.unsorted, 0, len(self.unsorted) - 1)
        assert_that(_sorted).is_equal_to(self.sorted)

    def test_selection_sort(self):
        _sorted = selectionsort(self.unsorted)
        assert_that(_sorted).is_equal_to(self.sorted)

    def test_radix_sort(self):
        pass



