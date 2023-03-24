from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".csv"):
            with open(path) as file:
                list_of_dicts = [dict(row) for row in csv.DictReader(file)]
                return list_of_dicts
        else:
            raise ValueError("Arquivo inválido")
