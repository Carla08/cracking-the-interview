class LinkedList:
    def __init__(self, head):
        self._head = head

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    def insert(self, node):
        n = self.get_last_node()
        n.nxt = node

    def find(self, value):
        node = self.head
        while node.nxt:
            if node.value == value:
                return node
            node = node.nxt
        return node if node.value == value else None

    def remove(self, value):
        n = self.head
        if n.value == value:
            return n
        else:
            while n.nxt:
                if n.nxt.value == value:
                    if n.nxt.nxt:
                        n.nxt = n.nxt.nxt
                    else:
                        # removal is last or head
                        n.nxt = None
                    return True
                n = n.nxt
            raise ValueError(f'Node with value {value} not found in list')

    def get_last_node(self):
        n = self.head
        while n.nxt:
            n = n.nxt
        return n

    def __repr__(self):
        n = self.head
        s = ''
        while n.nxt:
            s += f'{n.value}, '
            n = n.nxt
        s += f'{n.value}'
        return s

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
        if not self.n:
            raise StopIteration
        else:
            val = self.n.value
            self.n = self.n.nxt
            return val
