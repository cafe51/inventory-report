from abc import ABC, abstractmethod
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data():
        raise NotImplementedError

    @staticmethod
    def generate(list_of_dicts, type):
        if type == "simples":
            return SimpleReport.generate(list_of_dicts)
        elif type == "completo":
            return CompleteReport.generate(list_of_dicts)
        else:
            raise TypeError(f"{type} não pode ser aceito: VALOR ERRADO")
