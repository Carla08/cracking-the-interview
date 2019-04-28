from data_structures.trees.tree import Tree
from data_structures.trees.binary_tree_node import Node
from data_structures.trees.tree_traversals import inorder, preorder

class BinarySearchTree(Tree):

    def insert(self, value):
        pointer = None
        node = self.root
        new_node = Node(value)
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

    def remove(self, value, node=None):
        """
        Removal has 3 possible cases:
            1-. The node at value has no childs:  find the parent and point it's child to None
            2-. The node has one child: Elevate the child to occupy the node's place
            3-. The node has two childs: Tricky case! Check the notes.
        :param value:
        :return:
        """
        # find parent node
        parent = self.find_parent(value, node)
        # TODO: check when parent is None. Tree's root.
        is_node_left_child = parent.left == value  # to check weather the value is left or right
        node = parent.left if parent.left == value else parent.right

        if self.is_node_leaf(node):
            self._remove_leaf(parent, is_node_left_child)
        elif self.is_node_two_childs(node):
            self._remove_node_with_two_childs(node)
        else:
            # case 2: node has one child
            self._remove_node_with_one_child(parent, node, is_node_left_child)

    def is_node_leaf(self, node):
        return not node.left and not node.right

    def is_node_two_childs(self, node):
        return node.left and node.right

    def get_node_only_child(self, node):
        if not self.is_node_two_childs(node):
            return node.left or node.right
        else:
            print("Warning, node has two childs.")

    def _remove_leaf(self, parent, is_node_left: bool):
        if is_node_left:
            parent.left = None
        else:
            parent.right = None

    def _remove_node_with_one_child(self, parent, node, is_node_left: bool):
        child = self.get_node_only_child(node)
        if is_node_left:
            parent.left = child
        else:
            parent.right = child

    def _remove_node_with_two_childs(self, node):
        succesor = self.get_min(node.right)
        node.value = succesor.value
        duplicated = self.find(node.value, node.right)
        self.remove(duplicated.value, node)

    def find(self, value, node=None):
        node = self.root if not node else node
        return self.binary_search(node, value)

    def binary_search(self, node, value):
        while node and value != node.value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def get_max(self, node=None):
        node = self.root if not node else node
        while node.right:
            node = node.right
        return node

    def get_min(self, node=None):
        node = self.root if not node else node
        while node.left:
            node = node.left
        return node

    def _get_node_childs_values(self, node):
        if node.right and node.left:
            return [node.right, node.left]
        elif not node.right and not node.left:
            return []
        else:
            return [node.right or node.left]

    def find_parent(self, value, node=None):
        node = self.root if not node else node
        while node.right or node.left:
            child_values = self._get_node_childs_values(node)
            if value in child_values:
                return node
            else:
                node = node.left if value < node.left.value else node.right

        return node

    def to_max_heap(self, node):
        # on a binary tree the max val is always on the bottom most right most leaf.
        # the order would be:
        # right, visit, left
        # kind of a weird inorder.
        if node:
            yield from self.to_max_heap(node.right)
            yield node
            yield from self.to_max_heap(node.left)

    def find_lowest_common_ancestor(self, node_a, node_b):
        """
        Return the root of a subtree which both node A and B exist. This subtree
        should be the smallest subtree possible.
        """
        def find_lca_helper(node):
            if not node:
                return
            elif node == node_a or node == node_b:
                return node
            else:
                node_left = find_lca_helper(node.left)
                node_right = find_lca_helper(node.right)
                return node if node_left and node_right else node_left or node_right

        return find_lca_helper(self.root)

    def serialize(self):
        inorder_lst = [n.value for n in inorder(self.root)]
        preorder_lst = [n.value for n in preorder(self.root)]
        return {'inorder': inorder_lst, 'preorder': preorder_lst}

    @staticmethod
    def deserialize(inorder_lst, preorder_lst):
        # inorder : 1,2,3,4,5,6,7
        # preorder: 4,2,1,3,6,5,7
        def reconstruct(in_lst, pre_lst, prev_val):
            if not pre_lst:
                return

            lft_inodr, right_inodr = [], []
            lft_preord, right_preord = [], []
            n = pre_lst[0]
            node = Node(n)
            for in_n, pre_n in zip(in_lst, pre_lst):
                if in_n < n:
                    lft_inodr.append(in_n)
                if in_n > n:
                    right_inodr.append(in_n)
                if pre_n < n:
                    lft_preord.append(pre_n)
                if pre_n > n:
                    right_preord.append(pre_n)

            node.left = reconstruct(lft_inodr, lft_preord, n)
            node.right = reconstruct(right_inodr, right_preord, n)

            return node

        return BinarySearchTree(reconstruct(inorder_lst, preorder_lst, preorder_lst[0]))









