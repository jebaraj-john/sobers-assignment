import abc
from UnifiedStmt import UnifiedStmt

class AbsOutFormat(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, unified_stmts: list[UnifiedStmt]):
        pass