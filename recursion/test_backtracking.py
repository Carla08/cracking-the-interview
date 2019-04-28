import unittest
from recursion.backtracking import get_power_set, get_all_binary, dice_sum, telephone_to_word
from assertpy import assert_that

class TestBacktracking(unittest.TestCase):
    def setUp(self):
        pass

    def test_power_set(self):
        _set = {1,2,3}
        expected = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
        for _set in get_power_set(_set, set()):
            is_expected = list(_set) in expected
            assert_that(is_expected).is_true()

    def test_get_all_binary(self):
        digits = 2
        expected = ['00', '01', '10', '11']
        for binary_str in get_all_binary(digits, ''):
            is_expected = binary_str in expected
            assert_that(is_expected).is_true()

    def test_dice_sum(self):
        dices = 5
        _sum = 12
        # watch the magic. I figured out this problem by myself. It's pretty sick.
        # yeah.
        dice_sum(dices, _sum, [])

    def test_telephone_to_word(self):
        word = "toocool"
