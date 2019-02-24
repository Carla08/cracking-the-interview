from assertpy import assert_that
from data_structures.linked_lists.utils import create_linked_list_with_list_of_values, \
    create_linked_list_with_list_of_nodes
from data_structures.linked_lists.node_lists_problems import reverse_linked_list, \
    find_intersection_of_linked_lists, find_list_circular_node, remove_nth_from_end
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

    def test_list_circular(self):
        circular_lst = self._get_circular_lst()
        circular_node = find_list_circular_node(circular_lst)
        assert_that(1000).is_equal_to(circular_node.value)

    def test_remove_nth_from_end(self):
        expected_lst_vals = [1,2,3,5]
        new_node = remove_nth_from_end(self.lst.head, 2)
        for i in range(4):
            assert_that(new_node.value).is_equal_to(expected_lst_vals[i])
            new_node = new_node.nxt

    def _get_multiple_intersected_lists(self):
        common_node = Node(1000)
        nodes_a = [Node(1), Node(2), Node(3), Node(4), common_node, Node(6)]
        nodes_b= [Node(7), Node(8), common_node, Node(9)]
        list_a = create_linked_list_with_list_of_nodes(nodes_a)
        list_b = create_linked_list_with_list_of_nodes(nodes_b)
        return [list_a, list_b]

    def _get_circular_lst(self):
        circular_node = Node(1000)
        nodes = [Node(1), Node(2), circular_node, Node(3), circular_node]
        return create_linked_list_with_list_of_nodes(nodes)

