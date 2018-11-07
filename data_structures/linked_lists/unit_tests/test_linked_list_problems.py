from assertpy import assert_that
from data_structures.linked_lists.utils import create_linked_list_with_list_of_values
from data_structures.linked_lists.node_lists_problems import reverse_linked_list
import unittest

class TestLinkedListProblems(unittest.TestCase):
    def setUp(self):
        self.values = [1,2,3,4,5]
        self.lst = create_linked_list_with_list_of_values(self.values)

    def test_reverse_linked_list(self):
        reversed_nums = self.values
        reversed_nums.reverse()
        reversed_list = reverse_linked_list(self.lst)
        for rev_val, rev_n in zip(reversed_list, reversed_nums):
            assert_that(rev_val).is_equal_to(rev_n)
