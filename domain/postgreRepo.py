from typing_extensions import override

from api_models.loanApplication import LoanApplication
from domain.interfaces.iPostgreRepo import IPostgreRepo
from infrastructure.interfaces.iPostgreDb import IPostgreDb


class PostgreRepo(IPostgreRepo):
    def __init__(self, postgre_db: IPostgreDb):
        self._postgre_db = postgre_db

    @override
    async def status(self, applicant_id: str):
        # todo: get status from db
        # return await self._postgre_db.exec('get status query')
        return 'approved'

    @override
    async def save(self, loan_application: LoanApplication, status: str):
        # todo: save applicaton to db
        await self._postgre_db.exec('insert into db')