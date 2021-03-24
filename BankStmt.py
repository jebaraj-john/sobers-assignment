from AbsBankFormat import AbsBankFormat
from UnifiedStmt import UnifiedStmt
import csv

class BankStmt:
    def __init__(self, banks :dict, outputFormat):
        self.banks = banks
        self.outputFormat = outputFormat

    def _read_stmt(self, bank: AbsBankFormat, file: str) -> UnifiedStmt:
        unified_stmt = None
        with open(file) as csv_file:
            bankstmts = reader = csv.DictReader(csv_file)
            unified_stmts = bank.read(bankstmts)

        return unified_stmts

    def transform(self, csv_files: dict):
        unified_stms = []
        for csv_file in csv_files:
            csv_bank = csv_file['bank_type']
            if (csv_bank in self.banks):
                data = self._read_stmt(self.banks[csv_bank], csv_file['filename'])
                unified_stms = unified_stms + data
            else:
                raise Exception('{} bank.type.is.not.configured'.format(csv_bank))

        self.outputFormat.write(unified_stms)
