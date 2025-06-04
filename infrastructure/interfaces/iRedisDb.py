from __future__ import annotations

from abc import ABC, abstractmethod


class IRedisDb(ABC):

    @abstractmethod
    async def get(self, key: str) -> str | None:
        pass

    @abstractmethod
    async def set(self, key: str, value: str):
        pass
