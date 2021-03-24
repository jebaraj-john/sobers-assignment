from BankStmt import BankStmt
from CsvOut import CsvOut
from Bank1 import Bank1
from Bank2 import Bank2
from Bank3 import Bank3

csv_out = CsvOut('./data/out/unified_stmt.csv')
banks = {
    'bank1': Bank1(),
    'bank2': Bank2(),
    'bank3': Bank3()
}

bank_stmt = BankStmt(banks, csv_out)
bank_stmt.transform([
    {
        'bank_type': 'bank1',
        'filename': './data/bank1.csv',
    },
    {
        'bank_type': 'bank2',
        'filename': './data/bank2.csv',
    },
    {
        'bank_type': 'bank3',
        'filename': './data/bank3.csv',
    }
])