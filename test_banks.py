import unittest
from Bank1 import Bank1
from Bank2 import Bank2
from Bank3 import Bank3
from UnifiedStmt import UnifiedStmt
from datetime import datetime


class TestBank1(unittest.TestCase):
    def test_reads_data(self):
        expected_out = UnifiedStmt()
        date = datetime.strptime('Oct 1 2019', '%b %d %Y')
        expected_out.set_date(date)
        expected_out.set_transaction_type('remove')
        expected_out.set_amount('99.20')
        expected_out.set_from('198')
        expected_out.set_to('182')

        input = [{
            'timestamp': 'Oct 1 2019',
            'type': 'remove',
            'amount': '99.20',
            'from': '198',
            'to': '182'
        }]
        bank = Bank1()
        unifined_stmts = bank.read(input)
        self.assertEqual(len(unifined_stmts), 1)
        self.assertEqual(unifined_stmts[0].get_dict(), expected_out.get_dict())


class TestBank2(unittest.TestCase):
    def test_reads_data(self):
        expected_out = UnifiedStmt()
        date = datetime.strptime('03-10-2019', '%d-%m-%Y')
        expected_out.set_date(date)
        expected_out.set_transaction_type('add')
        expected_out.set_amount('99.20')
        expected_out.set_from('198')
        expected_out.set_to('182')

        input = [{
            'date': '03-10-2019',
            'transaction': 'add',
            'amounts': '99.20',
            'from': '198',
            'to': '182'
        }]
        bank = Bank2()
        unifined_stmts = bank.read(input)
        self.assertEqual(len(unifined_stmts), 1)
        self.assertEqual(unifined_stmts[0].get_dict(), expected_out.get_dict())

class TestBank3(unittest.TestCase):
    def test_reads_data(self):
        expected_out = UnifiedStmt()
        date = datetime.strptime('5 Oct 2019', '%d %b %Y')
        expected_out.set_date(date)
        expected_out.set_transaction_type('remove')
        expected_out.set_amount('5.07')
        expected_out.set_from('198')
        expected_out.set_to('182')

        input = [{
            'date_readable': '5 Oct 2019',
            'type': 'remove',
            'euro': '5',
            'cents': '7',
            'from': '198',
            'to': '182'
        }]
        bank = Bank3()
        unifined_stmts = bank.read(input)
        self.assertEqual(len(unifined_stmts), 1)
        self.assertEqual(unifined_stmts[0].get_dict(), expected_out.get_dict())



if __name__ == '__main__':
    unittest.main()
