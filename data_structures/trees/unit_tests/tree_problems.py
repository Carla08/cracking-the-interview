import unittest
from assertpy import assert_that
from data_structures.trees.tree_problems import sum_range


class TreeProblems(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_range(self):
        nums = [-2, 5, -1]
        lower = -2
        upper = 2
        result = sum_range(nums, lower, upper)
        expected = [[0, 0], [2, 2], [0, 2]]
        assert_that(result).is_equal_to(expected)


