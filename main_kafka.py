from di import DI
import asyncio
from domain.interfaces.iKafkaRepo import IKafkaRepo
from usecases.interfaces.iProcessApplicationUseCase import IProcessApplicationUseCase


class KafkaTopicConsumer:
    def __init__(self, kafka_repo: IKafkaRepo, use_case: IProcessApplicationUseCase):
        self._kafka_repo = kafka_repo
        self._use_case = use_case

    async def consume(self):
        result_list = []
        for loanApplication in self._kafka_repo.pop():
            print(f'get from kafka topic [{loanApplication}]')
            result = await self._use_case.execute(loanApplication)
            result_list.append(result)
        return result_list


if __name__ == '__main__':
    async def task():
        return await KafkaTopicConsumer(
            DI().kafka_repo(),
            DI().process_application_usecase()
        ).consume()


    useCaseResults = asyncio.run(task())
    print(f'process results: {useCaseResults}')
