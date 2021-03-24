from datetime import datetime
from collections import OrderedDict

class UnifiedStmt:
    def __init(self):
        self.transaction_type = None
        self.amount = None
        self.from_acc = None
        self.to_acc = None
        self.date = None

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def set_amount(self, amount):
        self.amount = amount

    def set_from(self, from_acc):
        self.from_acc = from_acc

    def set_to(self, to_acc):
        self.to_acc = to_acc

    def set_date(self, date):
        self.date = date

    def get_dict(self):
        return OrderedDict([
            ('date', self.date.strftime('%d-%m-%Y')),
            ('transaction_type', self.transaction_type),
            ('amount', self.amount),
            ('from_acc', self.from_acc),
            ('to_acc', self.to_acc),
        ])