
class SimpleQueue:
    def __init__(self, arr=None):
        self.arr = arr if arr else []
        self.first = None if not arr else 0
        self.last = None if not arr else len(arr) - 1

    def push(self, value):
        if not self.last:
            self.last = 0
            self.first = 0
        self.last += 1
        self.arr.append(value)

    def pop(self):
        if self.first >= len(self.arr) or self.first is None:
            raise QueueUnderflow
        _pop = self.arr[self.first]
        self.first += 1
        return _pop

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.pop()
        except QueueUnderflow:
            raise StopIteration

    def __repr__(self):
        return str(self.arr[self.first:])

class QueueUnderflow(IndexError):
    pass