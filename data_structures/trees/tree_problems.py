from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.binary_tree_node import Node


def sum_range(nums, lower, upper):
    """
    Given an integer array nums, return the number of range sums that
    lie in [lower, upper] inclusive.
    Range sum S(i, j) is defined as the sum of the elements in nums
    between indices i and j (i ≤ j), inclusive.

    A naive algorithm of O(n2) is trivial. You MUST do better than that.

    Example:

    Input: nums = [-2,5,-1], lower = -2, upper = 2,
    Output: 3
    Explanation: The three ranges are : [0,0], [2,2], [0,2] and their
    respective sums are: -2, -1, 2.
    """
    # create custom
    class SumBinarySearchTree(BinarySearchTree):

        def insert(self, value, index):
            pointer = None
            node = self.root
            new_node = SumNode(value, index)
            while node:
                pointer = node
                if value < node.value:
                    node = node.left
                else:
                    node = node.right
            if not pointer:
                # the tree is empty
                self.root = new_node
            elif value < pointer.value:
                pointer.left = new_node
            else:
                pointer.right = new_node

    class SumNode(Node):
        def __init__(self, value, index):
            super().__init__(value)
            self.index = index

    results = []
    sum_tree = SumBinarySearchTree()
    for i, num in enumerate(nums):
        sum_tree.insert(num, i)

    node = sum_tree.root
    while node:
        if lower > node.value > upper:
            results.append([node.index])
        

