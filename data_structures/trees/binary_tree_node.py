class Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right

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
