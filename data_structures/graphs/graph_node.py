class Node:
    def __init__(self, value):
        self._value = value
        self._neighbors = []
        self._marked = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors):
        self._neighbors = neighbors

    @property
    def marked(self):
        return self._marked

    @marked.setter
    def marked(self, marked):
        self._marked = marked

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Node):
            self._neighbors.append(neighbor)
        elif isinstance(neighbor, list):
            self._neighbors.extend(neighbor)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.value
        elif not isinstance(other, Node):
            print(f'{str(other)} not Node or Int')
            return False
        else:
            return other.value == self.value

    def __hash__(self):
        # until I find a better hash
        return self.value
