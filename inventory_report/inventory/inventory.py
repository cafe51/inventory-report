from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, type):
        list_of_dicts = []
        with open(path) as file:
            list_of_dicts = [dict(row) for row in csv.DictReader(file)]
        if type == "simples":
            return SimpleReport.generate(list_of_dicts)
        elif type == "completo":
            return CompleteReport.generate(list_of_dicts)
        else:
            raise TypeError(f"{type} não pode ser aceito: VALOR ERRADO")
