import unittest
from assertpy import assert_that
from data_structures.trees.tree import Tree
from data_structures.trees.tree_node import Node
import data_structures.trees.tree_traversals as traversals

class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.root = self.create_test_root()
        self.tree = MockTree(self.root)

    def test_inorder(self):
        inorder_order = [1, 2, 3, 4, 5, 6, 7]
        for i, node in enumerate(traversals.inorder(self.root)):
            assert_that(inorder_order[i]).is_equal_to(node.value)

    def test_preorder(self):
        preorder_order = [4, 2, 1, 3, 6, 5, 7]
        for i, node in enumerate(traversals.preorder(self.root)):
            assert_that(preorder_order[i]).is_equal_to(node.value)

    def test_postorder(self):
        postorder_order = [1, 3, 2, 5, 7, 6, 4]
        for i, node in enumerate(traversals.postorder(self.root)):
            assert_that(postorder_order[i]).is_equal_to(node.value)


    def create_test_root(self):
        root = Node(4)
        root.left, root.right = Node(2), Node(6)
        root.left.left, root.left.right = Node(1), Node(3)
        root.right.left, root.right.right = Node(5), Node(7)
        return root


class MockTree(Tree):
    def insert(self, value):
        pass

    def remove(self, value):
        pass
