from api_models.loanApplication import LoanApplication
from domain.interfaces.iPostgreRepo import IPostgreRepo
from domain.interfaces.iRedisRepo import IRedisRepo
from usecases.interfaces.iProcessApplicationUseCase import IProcessApplicationUseCase
from usecases.useCaseResult import UseCaseResult


class ProcessApplicationUseCase(IProcessApplicationUseCase):
    def __init__(self, postgre_repo: IPostgreRepo, redis_repo: IRedisRepo):
        self._postgre_repo = postgre_repo
        self._redis_repo = redis_repo

    async def execute(self, loan_application: LoanApplication) -> UseCaseResult:
        try:
            if loan_application.amount > 0 and \
                    1 <= loan_application.term_months <= 60:
                status = "approved"
            else:
                status = "rejected"

            await self._postgre_repo.save(loan_application, status)
            await self._redis_repo.save(loan_application, status)
            return UseCaseResult(True, "Application processed", status)

        except Exception as e:
            return UseCaseResult(False, f"Error: {str(e)}")
