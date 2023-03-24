from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list_of_dicts):
        self.list_of_dicts = list_of_dicts
        self.counter = 0

    def __next__(self):

        data = self.list_of_dicts[self.counter]

        if not data:
            raise StopIteration()

        self.counter += 1
        return data
