from domain.interfaces.iKafkaRepo import IKafkaRepo
from domain.interfaces.iPostgreRepo import IPostgreRepo
from domain.interfaces.iRedisRepo import IRedisRepo
from domain.kafkaRepo import KafkaRepo
from domain.postgreRepo import PostgreRepo
from domain.redisRepo import RedisRepo
from infrastructure.interfaces.iKafkaTopic import IKafkaTopic
from infrastructure.interfaces.iPostgreDb import IPostgreDb
from infrastructure.interfaces.iRedisDb import IRedisDb
from infrastructure.kafkaTopic import KafkaTopic
from infrastructure.postgreDb import PostgreDb
from infrastructure.redisDb import RedisDb
from usecases.getApplicationStatusUseCase import GetApplicationStatusUseCase
from usecases.interfaces.iGetApplicationStatusUseCase import IGetApplicationStatusUseCase
from usecases.interfaces.iProcessApplicationUseCase import IProcessApplicationUseCase
from usecases.interfaces.iSubmitApplicationUseCase import ISubmitApplicationUseCase
from usecases.processApplicationUseCase import ProcessApplicationUseCase

from usecases.submitApplicationUseCase import SubmitApplicationUseCase


class DI:
    def postgre_db(self) -> IPostgreDb:
        return PostgreDb()

    def postgre_repo(self) -> IPostgreRepo:
        return PostgreRepo(self.postgre_db())

    def redis_db(self) -> IRedisDb:
        return RedisDb()

    def redis_repo(self) -> IRedisRepo:
        return RedisRepo(self.redis_db())

    def kafka_topic(self) -> IKafkaTopic:
        return KafkaTopic()

    def kafka_repo(self) -> IKafkaRepo:
        return KafkaRepo(self.kafka_topic())

    def submit_application_usecase(self) -> ISubmitApplicationUseCase:
        return SubmitApplicationUseCase(self.kafka_topic())

    def process_application_usecase(self) -> IProcessApplicationUseCase:
        return ProcessApplicationUseCase(self.postgre_repo(), self.redis_repo())

    def get_application_status_usecase(self) -> IGetApplicationStatusUseCase:
        return GetApplicationStatusUseCase(self.postgre_repo(), self.redis_repo())
