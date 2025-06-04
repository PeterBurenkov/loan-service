from abc import ABC, abstractmethod
from collections.abc import Generator
from api_models.loanApplication import LoanApplication


class IKafkaRepo(ABC):

    @abstractmethod
    async def push(self, loan_application: LoanApplication):
        pass

    @abstractmethod
    def pop(self) -> Generator[LoanApplication]:
        pass
