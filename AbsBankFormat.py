import abc
from UnifiedStmt import UnifiedStmt

class AbsBankFormat(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self) -> list[UnifiedStmt]:
        pass