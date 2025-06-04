import asyncio

from typing_extensions import override

from infrastructure.interfaces.iPostgreDb import IPostgreDb


class PostgreDb(IPostgreDb):

    @override
    async def exec(self, query, params=None):
        await asyncio.sleep(1)  # Simulate delay
        # todo implement query over db (direct/sqlAlchemy/SqlModel)
        # try:
        #     conn = self._connection_pool.connection()
        #     cur = conn.cursor()
        #     cur.execute(query, params)
        #     result = cur.fetchall()
        #     cur.close()
        #     return result
        # finally:
        #     if conn is not None:
        #         conn.close()
