from data_structures.graphs.graph_node import Node
from typing import Set
from data_structures.queue.simple_queue import SimpleQueue
class Graph:
    def __init__(self, pointer=None):
        self._pointer = pointer
        self._pointers = {}

    def set_pointer(self, name, pointer):
        self._pointers[name] = pointer

    def get_pointer(self, name):
        return self._pointers[name]

    def breadth_first(self, node=None):
        node = self._pointer if not node else node
        queue = SimpleQueue()
        queued = {node}
        queue.push(node)

        for _node in queue:
            yield(_node)
            for n in _node.neighbors:
                if n not in queued:
                    queue.push(n)
                    queued.add(n)

    def depth_first(self, marked: Set, node=None):
        if not node:
            return
        else:
            marked.add(node)
            yield(node)
            for _node in node.neighbors:
                if _node not in marked:
                    yield from self.depth_first(marked, _node)

    def adjancy_matrix(self):
        pass

    def __repr__(self):
        return self.adjancy_matrix()


