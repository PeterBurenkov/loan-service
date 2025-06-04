from typing_extensions import override

from api_models.loanApplication import LoanApplication
from domain.interfaces.iRedisRepo import IRedisRepo
from infrastructure.interfaces.iRedisDb import IRedisDb


class RedisRepo(IRedisRepo):
    def __init__(self, redis_db: IRedisDb):
        self._redis_db = redis_db

    @override
    async def status(self, applicant_id: str):
        return await self._redis_db.get(applicant_id)

    @override
    async def save(self, loan_application: LoanApplication, status: str):
        await self._redis_db.set(loan_application.applicant_id, status)
