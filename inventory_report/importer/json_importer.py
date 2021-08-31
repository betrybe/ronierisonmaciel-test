import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if filepath.endswith(".json") is not True:
            raise ValueError("Arquivo inválido")
        try:
            with open(filepath, 'r') as file:
                storage = json.load(file)
                content = []
                for data in storage:
                    content.append(data)
                return content
        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
