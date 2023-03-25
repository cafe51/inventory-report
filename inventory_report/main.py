from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def define_instance(path):
    if path.endswith(".json"):
        return InventoryRefactor(JsonImporter)
    if path.endswith(".csv"):
        return InventoryRefactor(CsvImporter)
    if path.endswith(".xml"):
        return InventoryRefactor(XmlImporter)
    else:
        raise ValueError("Arquivo inválido")


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        _, caminho_do_arquivo_input, tipo_de_relatório, *others = sys.argv

        instance = define_instance(caminho_do_arquivo_input)

        response = instance.import_data(
            caminho_do_arquivo_input, tipo_de_relatório
        )
        print(response, end="")

