from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def generate(list_of_dicts, type):
        if type == "simples":
            return SimpleReport.generate(list_of_dicts)
        elif type == "completo":
            return CompleteReport.generate(list_of_dicts)
        else:
            raise TypeError(f"{type} não pode ser aceito: VALOR ERRADO")

    @staticmethod
    def import_data(path, type):
        if path.endswith(".json"):
            return Inventory.generate(JsonImporter.import_data(path), type)
        if path.endswith(".csv"):
            return Inventory.generate(CsvImporter.import_data(path), type)
        if path.endswith(".xml"):
            return Inventory.generate(XmlImporter.import_data(path), type)
        else:
            raise ValueError("Arquivo inválido")
