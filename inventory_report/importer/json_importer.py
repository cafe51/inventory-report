from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".json"):
            with open(path) as file:
                list_of_dicts = [dict(row) for row in json.load(file)]
            return list_of_dicts
        else:
            raise ValueError("Arquivo inválido")
