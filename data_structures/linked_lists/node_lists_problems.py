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



