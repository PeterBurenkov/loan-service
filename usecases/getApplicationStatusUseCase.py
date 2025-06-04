from typing_extensions import override
from domain.interfaces.iPostgreRepo import IPostgreRepo
from domain.interfaces.iRedisRepo import IRedisRepo
from usecases.interfaces.iGetApplicationStatusUseCase import IGetApplicationStatusUseCase
from usecases.useCaseResult import UseCaseResult


class GetApplicationStatusUseCase(IGetApplicationStatusUseCase):
    def __init__(self, postgre_repo: IPostgreRepo, redis_repo: IRedisRepo):
        self._postgre_repo = postgre_repo
        self._redis_repo = redis_repo

    @override
    async def execute(self, applicant_id: str):
        try:
            status = await self._redis_repo.status(applicant_id)
            if status is None:
                status = await self._postgre_repo.status(applicant_id)

            if status is not None:
                return UseCaseResult(True, "Status found", status)
            return UseCaseResult(False, "Failed to find status")
        except Exception as e:
            return UseCaseResult(False, f"Error: {str(e)}")
