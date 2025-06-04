from collections.abc import Generator
from typing_extensions import override

from infrastructure.interfaces.iKafkaTopic import IKafkaTopic


class KafkaTopic(IKafkaTopic):

    @override
    async def push(self, message):
        pass
        # todo implement publish to kafka
        # producer = aiokafka.AIOKafkaProducer(bootstrap_servers="localhost:9092")
        # await producer.start()
        # try:
        #     await producer.send_and_wait("my_topic", b"Super message")
        # finally:
        #     await producer.stop()

    @override
    def pop(self) -> Generator[str]:
        yield 'message1'
        # todo implement read from kafka
        # consumer = aiokafka.AIOKafkaConsumer(
        #     "my_topic",
        #     bootstrap_servers='localhost:9092'
        # )
        # await consumer.start()
        # try:
        #     async for msg in consumer:
        #         print(
        #             "{}:{:d}:{:d}: key={} value={} timestamp_ms={}".format(
        #                 msg.topic, msg.partition, msg.offset, msg.key, msg.value,
        #                 msg.timestamp)
        #         )
        # finally:
        #     await consumer.stop()
