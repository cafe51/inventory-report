from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str, type):
        if path.endswith(".xml"):
            with open(path) as file:
                list_of_dicts = xmltodict.parse(file.read())["dataset"][
                    "record"
                ]
                return Importer.generate(list_of_dicts, type)
        else:
            raise ValueError("Arquivo inválido")
