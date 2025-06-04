from typing_extensions import override

from api_models.loanApplication import LoanApplication
from infrastructure.interfaces.iKafkaTopic import IKafkaTopic
from usecases.interfaces.iSubmitApplicationUseCase import ISubmitApplicationUseCase
from usecases.useCaseResult import UseCaseResult


class SubmitApplicationUseCase(ISubmitApplicationUseCase):
    def __init__(self, kafka_topic: IKafkaTopic):
        self._kafka_topic = kafka_topic

    @override
    async def execute(self, loan_application: LoanApplication) -> UseCaseResult:
        try:
            await self._kafka_topic.push(loan_application)
            return UseCaseResult(True, "Loan application submitted")
        except Exception as e:
            return UseCaseResult(False, f"Error: {str(e)}")
