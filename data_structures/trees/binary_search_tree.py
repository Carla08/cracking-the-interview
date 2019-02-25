from data_structures.trees.tree import Tree
from data_structures.trees.binary_tree_node import Node

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
            childs = [node.right, node.left]
        elif not node.right and not node.left:
            childs = []
        else:
            childs = [node.right or node.left]
        return [] if not childs else [child.value for child in childs]

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





