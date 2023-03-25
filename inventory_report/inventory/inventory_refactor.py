from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def data_imported(self, path):
        self.data += self.importer.import_data(path)

    def import_data(self, path, fake_parameter):
        self.data_imported(path)

    def __iter__(self):
        return InventoryIterator(self.data)
