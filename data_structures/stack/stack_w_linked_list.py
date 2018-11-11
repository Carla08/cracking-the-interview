from data_structures.linked_lists.linked_list import LinkedList


class StackWLinkedList(LinkedList):
    def __init__(self, head, limit=None):
        super().__init__(head)
        self._tail = None
        self._limit = limit

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail):
        self._tail = tail

    def push(self, node):
        if self._limit and len(self) + 1 > self._limit:
            raise StackOverflow
        else:
            if self.tail:
                self.tail.nxt = node
                self._tail = node
            else:
                # first node inserted.
                self.head.nxt = node
                self._tail = node

    def pop(self):
        node = self.head
        if not node:
            raise StackUndeflow
        elif node.nxt is None:
            self._head = None
            return node
        else:
            while node:
                if node.nxt == self._tail:
                    tmp = self._tail
                    self._tail = node
                    self._tail.nxt = None
                    return tmp
                else:
                    node = node.nxt


    def insert(self, node):
        self.push(node)

class StackOverflow(IndexError):
    pass

class StackUndeflow(IndexError):
    pass