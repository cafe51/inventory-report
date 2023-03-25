from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.inventory.product import Product


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []
        self.products = []

    def data_imported(self, path):
        self.data = self.importer.import_data(path)
        # return self.data

    def import_data(self, path, fake_parameter):
        self.data_imported(path)
        list_of_dicts = self.data
        list_of_products = [
            Product(
                dictionary["id"],
                dictionary["nome_do_produto"],
                dictionary["nome_da_empresa"],
                dictionary["data_de_fabricacao"],
                dictionary["data_de_validade"],
                dictionary["numero_de_serie"],
                dictionary["instrucoes_de_armazenamento"],
            ).__repr__()
            for dictionary in list_of_dicts
        ]

        self.products = list_of_products

        return list_of_products

    def __iter__(self):
        return InventoryIterator(self.products)
