from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path_file, report_type):
        ext = path_file.split('.')[1]
        if ext == "json":
            data = JsonImporter().import_data(path_file)
        elif ext == "csv":
            data = CsvImporter().import_data(path_file)
        else:
            data = XmlImporter().import_data(path_file)
        return cls.generate(data, report_type)

    @classmethod
    def generate(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
