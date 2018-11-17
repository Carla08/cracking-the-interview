from data_structures.trees.tree_node import Node
from abc import abstractmethod

class Tree:
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    def find(self, value):
        raise NotImplementedError

    def levels(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError


