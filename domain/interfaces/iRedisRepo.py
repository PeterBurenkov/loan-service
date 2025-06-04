from abc import ABC, abstractmethod

from api_models.loanApplication import LoanApplication


class IRedisRepo(ABC):

    @abstractmethod
    async def status(self, applicant_id: str):
        pass

    @abstractmethod
    async def save(self, loan_application: LoanApplication, status: str):
        pass
