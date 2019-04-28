import unittest
from assertpy import assert_that
from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.binary_tree_node import Node
from data_structures.trees.tree_traversals import inorder

class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.root = self.create_test_root()
        self.tree = BinarySearchTree(self.root)

    def test_get_max(self):
        assert_that(7).is_equal_to(self.tree.get_max().value)

    def test_get_min(self):
        assert_that(1).is_equal_to(self.tree.get_min().value)

    def test_binary_search(self):
        find = self.tree.find(3)
        assert_that(find).is_not_none()

    def test_insert(self):
        self.tree.insert(8)
        inorder_order = [1, 2, 3, 4, 5, 6, 7, 8]
        for i, node in enumerate(inorder(self.root)):
            assert_that(inorder_order[i]).is_equal_to(node.value)

    def test_find_parent(self):
        parent = self.tree.find_parent(1)
        assert_that(2).is_equal_to(parent.value)

    def test_remove(self):
        self.tree.remove(6)
        inorder_order = [1, 2, 3, 4, 5, 7, 8]
        for i, node in enumerate(inorder(self.root)):
            assert_that(inorder_order[i]).is_equal_to(node.value)

    def test_to_max_heap(self):
        max_heap = [7, 6, 5, 4, 3, 2, 1]
        for i, node in enumerate(self.tree.to_max_heap(self.root)):
            assert_that(max_heap[i]).is_equal_to(node.value)

    def test_find_lowest_common_ancestor(self):
        node_a, node_b = Node(2), Node(5)
        expected_lca = Node(4)
        result_lca = self.tree.find_lowest_common_ancestor(node_a, node_b)
        assert_that(result_lca).is_equal_to(expected_lca)

    def test_reconstruct_tree(self):
        serialized_tree = self.tree.serialize()
        inorder_lst, preorder_lst = serialized_tree['inorder'], serialized_tree['preorder']
        reconstructed_tree = BinarySearchTree.deserialize(inorder_lst, preorder_lst)
        inorder_order = [1, 2, 3, 4, 5, 6, 7]
        for i, node in enumerate(inorder(reconstructed_tree.root)):
            assert_that(inorder_order[i]).is_equal_to(node.value)

    def create_test_root(self):
        root = Node(4)
        root.left, root.right = Node(2), Node(6)
        root.left.left, root.left.right = Node(1), Node(3)
        root.right.left, root.right.right = Node(5), Node(7)
        return root
