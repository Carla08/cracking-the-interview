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
        if not isinstance(other, Node):
            print(f'{str(other)} not Node')
            return False
        else:
            return True if other.value == self.value else False

    def __hash__(self):
        # until I find a better hash
        return self.value
