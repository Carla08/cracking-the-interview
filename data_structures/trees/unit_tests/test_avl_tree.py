import unittest
from assertpy import assert_that
from data_structures.trees.avl_tree import AVLTree
from data_structures.trees.binary_tree_node import Node
from data_structures.trees.tree_traversals import inorder

class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.root = self.create_test_root()
        self.tree = AVLTree(self.root)

    def test_height(self):
        assert_that(3).is_equal_to(self.tree.height(self.root))

    def test_calculate_balance_factor_unbalanced(self):
        unbalanced_root = self.create_unbalanced_root()
        unbalanced_tree = AVLTree(unbalanced_root)
        balance_factor = unbalanced_tree.calculate_balance_factor(unbalanced_root)
        assert_that(-2).is_equal_to(balance_factor)

    def test_calculate_balance_factor_balanced(self):
        balance_factor = self.tree.calculate_balance_factor(self.root)
        assert_that(0).is_equal_to(balance_factor)

    def test_is_balanced_false(self):
        unbalanced_root = self.create_unbalanced_root()
        unbalanced_tree = AVLTree(unbalanced_root)
        assert_that(unbalanced_tree.is_balanced()).is_false()

    def test_is_balanced_true(self):
        assert_that(self.tree.is_balanced()).is_true()
 
    def test_insert(self):
        pass

    def test_remove(self):
        pass

    def create_test_root(self):
        root = Node(4)
        root.left, root.right = Node(2), Node(6)
        root.left.left, root.left.right = Node(1), Node(3)
        root.right.left, root.right.right = Node(5), Node(7)
        return root

    def create_unbalanced_root(self):
        root = Node(6)
        root.left, root.right = Node(4), Node(7)
        root.left.left, root.left.right = Node(2), Node(5)
        root.left.left.left, root.left.left.right = Node(1), Node(3)
        return root
