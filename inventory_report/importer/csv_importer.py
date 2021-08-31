import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if filepath.endswith(".csv") is not True:
            raise ValueError("Arquivo inválido")
        try:
            with open(filepath) as file:
                storage = csv.DictReader(file, delimiter=",")
                content = []
                for data in storage:
                    content.append(data)
                return content
        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
