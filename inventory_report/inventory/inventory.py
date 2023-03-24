from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


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
    def import_data(path: str, type):
        if path.endswith(".csv"):
            with open(path) as file:
                list_of_dicts = [dict(row) for row in csv.DictReader(file)]
                return Inventory.generate(list_of_dicts, type)
        elif path.endswith(".json"):
            with open(path) as file:
                list_of_dicts = [dict(row) for row in json.load(file)]
                return Inventory.generate(list_of_dicts, type)
        elif path.endswith(".xml"):
            with open(path) as file:
                list_of_dicts = xmltodict.parse(file.read())["dataset"][
                    "record"
                ]
                return Inventory.generate(list_of_dicts, type)

        else:
            raise ValueError("CAMINHO ERRADO OU FORMATO DESCONHECIDO")
 