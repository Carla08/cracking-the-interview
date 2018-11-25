import unittest
from assertpy import assert_that
from data_structures.graphs.graph import Graph
from data_structures.graphs.graph_node import Node

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph_node = self.create_graph_node()
        self.graph = Graph(self.graph_node)

    def test_depth_first(self):
        expected = [1,2,6,5,4,3]
        marked = set()
        for i,node in enumerate(self.graph.depth_first(marked, self.graph_node)):
            assert_that(node.value).is_equal_to(expected[i])

    def test_breadth_first(self):
        expected = [1,2,4,5,6,3]
        for i, node in enumerate(self.graph.breadth_first(self.graph_node)):
            assert_that(node.value).is_equal_to(expected[i])

    def create_graph_node(self):
        node_1, node_2, node_3, node_4, node_5, node_6 = Node(1), Node(2),Node(3), Node(4), \
                                                         Node(5), Node(6)
        node_1.add_neighbor([node_2, node_4, node_5])
        node_2.add_neighbor([node_1, node_6, node_3])
        node_3.add_neighbor([node_2, node_6, node_4])
        node_4.add_neighbor([node_1, node_3, node_5])
        node_5.add_neighbor([node_4, node_6, node_1])
        node_6.add_neighbor([node_5, node_2, node_3])
        return node_1