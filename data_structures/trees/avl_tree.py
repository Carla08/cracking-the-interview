from data_structures.trees.binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):

    def insert(self, value):
        pass

    def remove(self, value, node=None):
        pass

    def is_balanced(self, node=None):
        node = self.root if not node else node
        balance_factor = self.calculate_balance_factor(node)
        return 1 > balance_factor > -1

    def calculate_balance_factor(self, node):
        """
        BalanceFactor(N) := Height(RightSubtree(N)) – Height(LeftSubtree(N))
        """
        return self.height(node.right) - self.height(node.left)

    def height(self, node=None):
        if not node:
            return 0
        else:
            right = self.height(node.right)
            left = self.height(node.left)
            return max(right, left) + 1



