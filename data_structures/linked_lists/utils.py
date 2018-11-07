from data_structures.linked_lists.linked_list import LinkedList
from data_structures.linked_lists.node_list import Node

def create_linked_list_with_list_of_values(values):
    linked_list = LinkedList(Node(values[0]))  # head
    for value in values[1:]:
        linked_list.insert(Node(value))
    return linked_list