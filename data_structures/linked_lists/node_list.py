class Node:
    def __init__(self, value):
        self._value = value
        self._nxt = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def nxt(self):
        return self._nxt

    @nxt.setter
    def nxt(self, nxt):
        self._nxt = nxt

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, Node):
            print(f'{str(other)} not Node')
            return False
        else:
            return True if other.value == self.value else False

    def __hash__(self):
        # until I find a better hash
        return self.value
