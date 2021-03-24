from AbsBankFormat import AbsBankFormat
from UnifiedStmt import UnifiedStmt
from datetime import datetime

class Bank3(AbsBankFormat):
    def read(self, bankstmts) -> list[UnifiedStmt]:
        result_stmt = []
        for row in bankstmts:
            unified_stmt = UnifiedStmt()
            unified_stmt.set_date(
                datetime.strptime(row['date_readable'], '%d %b %Y')
            )
            unified_stmt.set_transaction_type(row['type'])
            amount = int(row['euro']) + (int(row['cents']) / 100)
            unified_stmt.set_amount(str(amount))
            unified_stmt.set_from(row['from'])
            unified_stmt.set_to(row['to'])
            result_stmt.append(unified_stmt)

        return result_stmt
