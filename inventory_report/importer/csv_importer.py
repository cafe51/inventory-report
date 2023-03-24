from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str, type):
        if path.endswith(".csv"):
            with open(path) as file:
                list_of_dicts = [dict(row) for row in csv.DictReader(file)]
                return Importer.generate(list_of_dicts, type)
        else:
            raise ValueError("Arquivo inválido")
