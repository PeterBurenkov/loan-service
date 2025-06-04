from abc import ABC, abstractmethod


class IPostgreDb(ABC):

    @abstractmethod
    async def exec(self, query, params=None):
        pass
