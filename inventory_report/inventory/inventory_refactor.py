from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path_file, report_type):
        self.data.extend(self.importer.import_data(path_file))
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)
