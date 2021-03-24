from AbsBankFormat import AbsBankFormat
from UnifiedStmt import UnifiedStmt
from datetime import datetime

class Bank1(AbsBankFormat):
    def read(self, bankstmts) -> list[UnifiedStmt]:
        result_stmt = []
        for row in bankstmts:
            unified_stmt = UnifiedStmt()
            unified_stmt.set_date(
                datetime.strptime(row['timestamp'], '%b %d %Y')
            )
            unified_stmt.set_transaction_type(row['type'])
            unified_stmt.set_amount(row['amount'])
            unified_stmt.set_from(row['from'])
            unified_stmt.set_to(row['to'])
            result_stmt.append(unified_stmt)

        return result_stmt
