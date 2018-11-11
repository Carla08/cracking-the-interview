import unittest
from data_structures.stack.stack_w_linked_list import StackWLinkedList, StackUndeflow, StackOverflow
from data_structures.linked_lists.node_list import Node
from assertpy import assert_that

class TestStackWithLinkedList(unittest.TestCase):
    def setUp(self):
        self.stack = StackWLinkedList(Node(1))

    def test_push(self):
        self.stack.push(Node(2))
        assert_that(1).is_equal_to(self.stack.pop().value)

    def test_pop_one_element(self):
        assert_that(1).is_equal_to(self.stack.pop().value)

    def test_pop(self):
        self.stack.push(Node(2))
        self.stack.push(Node(3))
        assert_that(3).is_equal_to(self.stack.pop().value)

    def test_stack_underflow(self):
        self.stack.pop()
        with self.assertRaises(StackUndeflow):
            self.stack.pop()

    def test_overflow(self):
        stack_w_limit = StackWLinkedList(Node(1), 1)
        with self.assertRaises(StackOverflow):
            stack_w_limit.push(Node(2))


