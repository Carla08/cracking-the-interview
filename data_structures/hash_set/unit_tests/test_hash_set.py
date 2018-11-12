import unittest
from data_structures.hash_set.hash_set import HashSet
from assertpy import assert_that

class TestHashSet(unittest.TestCase):
    def setUp(self):
        self.hash_set = HashSet(max_len=10)

    def test_add(self):
        self.hash_set.add(11)
        assert_that(self.hash_set.contains(11)).is_true()

    def test_contains_true(self):
        self.hash_set.add(11)
        self.hash_set.add(13)
        assert_that(self.hash_set.contains(13)).is_true()

    def test_contains_false(self):
        assert_that(self.hash_set.contains(45)).is_false()

    def test_remove(self):
        self.hash_set.add(11)
        self.hash_set.remove(11)
        assert_that(self.hash_set.contains(11)).is_false()

    def test_iterator(self):
        self.hash_set.add(10)
        self.hash_set.add(12)
        self.hash_set.add(16)
        self.hash_set.add(19)
        self.hash_set.add(29)
        correct_order = [10,12,16,29,19]
        for i, item in enumerate(self.hash_set):
            assert_that(correct_order[i]).is_equal_to(item)

    def test_length(self):
        self.hash_set.add(11)
        assert_that(1).is_equal_to(len(self.hash_set))
