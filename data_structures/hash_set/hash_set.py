from data_structures.linked_lists.linked_list import LinkedList
from data_structures.linked_lists.node_list import Node

class HashSet:
    def __init__(self, max_len=10):
        self._array = [LinkedList() for _ in range(max_len)]
        self._max_len = max_len

    def add(self, value):
        hash = value.__hash__()
        index = hash % self._max_len
        linked_list = self._array[index]
        if linked_list.head is None:
            linked_list.head = Node(value)
        else:
            tmp = linked_list.head
            linked_list.head = Node(value)
            linked_list.head.nxt = tmp

    def contains(self, value):
        hash = value.__hash__()
        index = hash % self._max_len
        linked_list = self._array[index]
        try:
            return True if linked_list.find(value) else False
        except (ValueError, AttributeError):
            # not found in linked list
            return False

    def remove(self, value):
        hash = value.__hash__()
        index = hash % self._max_len
        linked_list = self._array[index]
        try:
            linked_list.remove(value)
        except (ValueError, AttributeError):
            # not found in linked list
            raise ValueError(f'{value} not found in hash set')

    def __iter__(self):
        self.n = self._array[0].head
        self.index = 0
        self.is_last_linked_list = False
        return self

    def __next__(self):
        if not self.n or not self.is_last_linked_list:
            raise StopIteration
        else:
            val = self.n.value
            if self.n.nxt:
                self.n = self.n.nxt
            else:
                self.index += 1
                try:
                    while not self._array[self.index].head:
                        self.index += 1
                    self.n = self._array[self.index].head
                except IndexError:
                    # no more lists
                    self.is_last_linked_list = True
            return val

    def __len__(self):
        return sum(len(lst) for lst in self._array)


