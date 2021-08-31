import xml.etree.ElementTree as Xtudo
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if filepath.endswith(".xml") is not True:
            raise ValueError("Arquivo inválido")
        with open(filepath, "r") as file:
            content = []
            tree = Xtudo.parse(file)
            root = tree.getroot()
            for data in root:
                node = dict()
                for sub in data:
                    node[sub.tag] = sub.text
                content.append(node)
            return content
