from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    _, path_file, report_type = sys.argv
    arq, ext = path_file.split(".")

    if ext == "json":
        file = InventoryRefactor(JsonImporter)
    elif ext == "csv":
        file = InventoryRefactor(CsvImporter)
    else:
        file = InventoryRefactor(XmlImporter)

    print(file.import_data(path_file, report_type), end='')
