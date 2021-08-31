from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterator):
        self._iterator = iterator
        self._index = 0

    def __next__(self):
        try:
            actual = self._iterator[self._index]
        except IndexError:
            raise StopIteration
        else:
            self._index += 1
        return actual
