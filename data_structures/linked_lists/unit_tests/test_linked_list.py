from data_structures.linked_lists.linked_list import LinkedList
from data_structures.linked_lists.node_list import Node
from assertpy import assert_that
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        head = Node(1)
        self.linked_list = LinkedList(head)

    def test_insert(self):
        new_node = Node(2)
        self.linked_list.insert(new_node)
        expected = 2
        result = self.linked_list.get_last_node().value
        assert_that(expected).is_equal_to(result)

    def test_find(self):
        self.linked_list.insert(Node(3))
        self.linked_list.insert(Node(4))
        result = self.linked_list.find(3)
        expected = Node(3)
        assert_that(expected.value).is_equal_to(result.value)

    def test_remove(self):
        self.linked_list.insert(Node(5))
        self.linked_list.insert(Node(6))
        result = self.linked_list.remove(5)
        assert_that(result).is_true()

    def test_remove_non_existing(self):
        self.linked_list.insert(Node(5))
        self.linked_list.insert(Node(6))
        with self.assertRaises(ValueError):
            self.linked_list.remove(100)

    def test_iteration(self):
        self.linked_list.insert(Node(2))
        self.linked_list.insert(Node(3))
        self.linked_list.insert(Node(4))
        numbers = [1,2,3,4]
        for val, num in zip(self.linked_list, numbers):
            assert_that(val).is_equal_to(num)
