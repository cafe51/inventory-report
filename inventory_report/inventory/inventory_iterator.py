from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self.products = products
        self.counter = 0

    def __next__(self):
        if self.counter >= len(self.products):
            raise StopIteration()

        data = self.products[self.counter]
        self.counter += 1
        return data
