from data_structures.linked_lists.linked_list import LinkedList
from data_structures.linked_lists.node_list import Node

def create_linked_list_with_list_of_values(values):
    linked_list = LinkedList(Node(values[0]))  # head
    for value in values[1:]:
        linked_list.insert(Node(value))
    return linked_list

def create_linked_list_with_list_of_nodes(nodes):
    linked_list = LinkedList(nodes[0])  # head
    for node in nodes[1:]:
        linked_list.insert(node)
    return linked_list