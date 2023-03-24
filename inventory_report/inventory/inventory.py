from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".json"):
            return JsonImporter.import_data(path, type)
        if path.endswith(".csv"):
            return CsvImporter.import_data(path, type)
        if path.endswith(".xml"):
            return XmlImporter.import_data(path, type)
        else:
            raise ValueError("Arquivo inválido")
