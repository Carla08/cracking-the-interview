from assertpy import assert_that
from data_structures.linked_lists.utils import create_linked_list_with_list_of_values, \
    create_linked_list_with_list_of_nodes
from data_structures.linked_lists.node_lists_problems import reverse_linked_list, \
    find_intersection_of_linked_lists
from data_structures.linked_lists.node_list import Node
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

    def test_lsts_intersection(self):
        lst_of_lsts = self._get_multiple_intersected_lists()
        common_node = find_intersection_of_linked_lists(lst_of_lsts)
        assert_that(1000).is_equal_to(common_node.value)

    def _get_multiple_intersected_lists(self):
        common_node = Node(1000)
        nodes_a = [Node(1), Node(2), Node(3), Node(4), common_node, Node(6)]
        nodes_b= [Node(7), Node(8), common_node, Node(9)]
        list_a = create_linked_list_with_list_of_nodes(nodes_a)
        list_b = create_linked_list_with_list_of_nodes(nodes_b)
        return [list_a, list_b]
