class SequentialIterator:
    def __init__(self, parent):
        self._index = 0
        self.parent = parent

    def next_index(self):
        if self._index < parent.max_index:
            self._index += 1
        else:
            raise StopIteration()
        return self._index
