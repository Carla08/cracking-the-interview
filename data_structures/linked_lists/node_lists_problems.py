from typing import List

def reverse_linked_list(lst):
    n = lst.head
    _next = None
    _prev = lst.head
    while n:
        _next = n.nxt
        n.nxt = _prev
        _prev = n
        n = _next

    lst.head.nxt = None
    lst.head = _prev
    return lst
####################################################################################################
def find_intersection_of_linked_lists(lst_of_lsts: List['LinkedList']):
    # get the shortest list
    shortest_len = min(len(lst) for lst in lst_of_lsts)

    # for each list set the pointer on the nth before last node
    for linked_list in lst_of_lsts:
        nth = (len(linked_list) - shortest_len) + 1
        linked_list.set_pointer('common', nth)

    # iter through all lst at the same time.
    nodes = get_all_lst_nodes(lst_of_lsts)
    while nodes:
        all_equal = check_all_nodes_equal(nodes)
        if all_equal:
            return nodes[0]  # any node will do, since they're all equal.
        else:
            nodes = get_all_lst_nodes(lst_of_lsts)

def get_all_lst_nodes(lst_of_lsts):
    nodes = []
    for lst in lst_of_lsts:
        common_pointer = lst.get_pointer('common')
        nodes.append(common_pointer)
        lst.update_pointer('common')  # move pointer one ahead
    return nodes

def check_all_nodes_equal(lst):
    return len(set(lst)) == 1

####################################################################################################

def find_list_circular_node(lst):
    # set quick n slow pointers
    lst.set_pointer('quick')
    lst.set_pointer('slow')

    #advance quick pointer.
    lst.update_pointer('quick', 2)

    try:
        while not lst.get_pointer('slow') == lst.get_pointer('quick'):
            lst.update_pointer('slow')
            lst.update_pointer('quick', 2)
        return lst.get_pointer('slow')  # or quick, since they're equal.
    except IndexError:
        return False # not a circular list.










