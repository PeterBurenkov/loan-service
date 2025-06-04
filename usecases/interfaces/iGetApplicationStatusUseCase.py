from abc import ABC, abstractmethod

from api_models.loanApplication import LoanApplication
from usecases.useCaseResult import UseCaseResult


class IGetApplicationStatusUseCase(ABC):

    @abstractmethod
    async def execute(self, applicant_id: str) -> UseCaseResult:
        pass