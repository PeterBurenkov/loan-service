from abc import ABC, abstractmethod
from collections.abc import Generator


class IKafkaTopic(ABC):

    @abstractmethod
    async def push(self, message):
        pass

    @abstractmethod
    def pop(self) -> Generator[str]:
        pass
