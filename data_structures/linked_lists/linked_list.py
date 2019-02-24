class LinkedList:
    def __init__(self, head=None):
        self._head = head
        self._pointers_dict = {}

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @property
    def pointers_dict(self):
        return self._pointers_dict

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
            self._head = n.nxt
            return True
        else:
            while n.nxt:
                if n.nxt.value == value:
                    if n.nxt.nxt:
                        n.nxt = n.nxt.nxt
                    else:
                        # removal is last
                        n.nxt = None
                    return True
                n = n.nxt
            raise ValueError(f'Node with value {value} not found in list')

    def get_nth_node(self, n):
        node = self.head
        for i in range(1,n):
            node = node.nxt
        return node

    def get_last_node(self):
        n = self.head
        while n.nxt:
            n = n.nxt
        return n

    def set_pointer(self, pointer_name, position=None):
        if position:
            self._pointers_dict[pointer_name] = self.get_nth_node(position)
        else:
            self._pointers_dict[pointer_name] = self.head

    def get_pointer(self, pointer_name):
        return self._pointers_dict[pointer_name]

    def update_pointer(self, pointer_name, steps=None):
        node = self._pointers_dict[pointer_name]
        if not steps:
            self.pointers_dict[pointer_name] = node.nxt
        else:
            for i in range(steps):
                if not node:
                    raise IndexError('End of list')
                else:
                    node = node.nxt
            self._pointers_dict[pointer_name] = node

    def __repr__(self):
        n = self.head
        if not n:
            return "Empty Linked List"
        s = ''
        while n.nxt:
            s += f'{n.value}, '
            n = n.nxt
        s += f'{n.value}'
        return s

    def __iter__(self, ith_node=None):
        self.n = ith_node if ith_node else self.head
        return self

    def __next__(self):
        if not self.n:
            raise StopIteration
        else:
            val = self.n.value
            self.n = self.n.nxt
            return val

    def __len__(self):
        n = self.head
        counter = 0
        while n:
            counter += 1
            n = n.nxt
        return counter


