from typing import List, TypeVar, Generic

from pydantic import BaseModel
from dal import DbHandler

T = TypeVar('T', bound=BaseModel)

class Controller(Generic[T]):
    def __init__(self, type_str: str):
        self.db_handler: DbHandler = DbHandler[T](type_str)
    async def get_all(self, id: str) -> List[T]:
        return await self.db_handler.get_all(id)
    
    async def delete(self, id: str) -> T:
        return await self.db_handler.delete(id)

    async def get(self, id: str) -> T:
        return await self.db_handler.get(id)

    async def put(self, id: str, obj_data: T) -> T:
        return await self.db_handler.put(id, obj_data)

    async def post(self, obj_data: T) -> T:
        return await self.db_handler.post(obj_data)