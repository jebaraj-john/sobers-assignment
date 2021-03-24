from UnifiedStmt import UnifiedStmt
from AbsOutFormat import AbsOutFormat
import csv

class CsvOut(AbsOutFormat):
    def __init__(self, filename):
        self.filename = filename

    def write(self, unified_stmts: list[UnifiedStmt]):
        with open(self.filename, mode='w+') as csv_file:
            fieldnames = ['date', 'transaction_type', 'amount', 'from_acc', 'to_acc']
            unified_writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            unified_writer.writeheader()
            for unified_stmt in unified_stmts:
                unified_writer.writerow(unified_stmt.get_dict())
