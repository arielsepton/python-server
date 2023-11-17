from typing import List, Generic
from common import T
from dal import DbHandlerBase


class Controller(Generic[T]):
    def __init__(self, db_handler: DbHandlerBase):
        self.db_handler: DbHandlerBase = db_handler

    async def get_all(self) -> List[T]:
        return await self.db_handler.get_all()

    async def delete(self, id: str) -> T:
        return await self.db_handler.delete(id)

    async def get(self, id: str) -> T:
        return await self.db_handler.get(id)

    async def put(self, id: str, obj_data: T) -> T:
        return await self.db_handler.put(id, obj_data)

    async def post(self, obj_data: T) -> T:
        return await self.db_handler.post(obj_data)