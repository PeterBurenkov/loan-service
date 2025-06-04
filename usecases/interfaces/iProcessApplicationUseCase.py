from abc import ABC, abstractmethod

from api_models.loanApplication import LoanApplication
from usecases.useCaseResult import UseCaseResult


class IProcessApplicationUseCase(ABC):

    @abstractmethod
    async def execute(self, loan_application: LoanApplication) -> UseCaseResult:
        pass