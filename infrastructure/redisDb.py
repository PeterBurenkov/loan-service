from __future__ import annotations

from typing_extensions import override

from infrastructure.interfaces.iRedisDb import IRedisDb
import asyncio


class RedisDb(IRedisDb):
    @override
    async def get(self, key: str) -> str | None:
        # todo implement communication with redis
        # Redis client bound to single connection (no auto reconnection).
        # redis = await aioredis.create_redis(
        #     'redis://localhost')
        # await redis.set('my-key', 'value')
        # val = await redis.get('my-key')
        # print(val)
        #
        # # gracefully closing underlying connection
        # redis.close()
        # await redis.wait_closed()

        if 'redis' in key:
            if 'approved' in key:
                return 'approved'
            return 'rejected'
        return None


    @override
    async def set(self, key: str, value: str):
        # todo implement communication with redis
        # Redis client bound to single connection (no auto reconnection).
        # redis = await aioredis.create_redis(
        #     'redis://localhost')
        # await redis.set('my-key', 'value')
        # val = await redis.get('my-key')
        # print(val)
        #
        # # gracefully closing underlying connection
        # redis.close()
        # await redis.wait_closed()
        # await asyncio.sleep(0.01)  # Simulate delay
        pass


if __name__ == '__main__':

    for key in ['redis approved', 'redis', 'postgre']:
        value = asyncio.run(RedisDb().get(key))
        print(f"(key, value) = ('{key}': '{value}')")
