import unittest
from data_structures.trees.tree import Tree
from data_structures.trees.tree_node import Node

class TestGenericTree(unittest.TestCase):
    def setUp(self):
        self.root = self.create_test_root()
        self.tree = MockTree(self.root)

    def create_test_root(self):
        root = Node(1)
        root.left, root.right = Node(2), Node(3)
        root.left.left, root.left.right = Node(4), Node(5)
        root.right.left, root.right.right = Node(6), Node(7)
        return root


class MockTree(Tree):
    def insert(self, value):
        pass

    def remove(self, value):
        pass
