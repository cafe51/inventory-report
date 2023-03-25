from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def data_imported(self, path):
        self.data += self.importer.import_data(path)

    def simple_or_completo(self, type):
        if type == "simples":
            return SimpleReport.generate(self.data)
        elif type == "completo":
            return CompleteReport.generate(self.data)
        else:
            raise TypeError(f"{type} não pode ser aceito: VALOR ERRADO")

    def import_data(self, path, type):
        self.data_imported(path)
        try:
            return self.simple_or_completo(type)
        except ValueError:
            raise ValueError("Arquivo inválido")

    def __iter__(self):
        return InventoryIterator(self.data)
