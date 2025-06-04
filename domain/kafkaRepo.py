from collections.abc import Generator
from typing_extensions import override

from api_models.loanApplication import LoanApplication
from domain.interfaces.iKafkaRepo import IKafkaRepo
from infrastructure.interfaces.iKafkaTopic import IKafkaTopic


class KafkaRepo(IKafkaRepo):
    def __init__(self, kafka_topic: IKafkaTopic):
        self._kafka_topic = kafka_topic

    @override
    async def push(self, loan_application: LoanApplication):
        await self._kafka_topic.push(loan_application)

    @override
    def pop(self) -> Generator[LoanApplication]:
         for message in self._kafka_topic.pop():
            #todo map message to the model
            yield LoanApplication(applicant_id='applicant_id1', amount=1000, term_months=15)
            yield LoanApplication(applicant_id='applicant_id2', amount=0, term_months=100)
