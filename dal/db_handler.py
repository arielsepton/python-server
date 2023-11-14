from typing import List, TypeVar, Generic

from pydantic import BaseModel
from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from db_connection import db
from common import NotFoundError


T = TypeVar('T', bound=BaseModel)


class DbHandler(Generic[T]):
    def __init__(self, type_str: str):
        self._collection = db[f"{type_str}_collection"]

        # self._logger: Logger = global_logger

    async def get_all(self) -> List[T]:
        return [T(**obj) async for obj in self._collection.find()]
    
    async def get(self, id: str) -> T:
        obj: dict = await self._collection.find_one({"_id": ObjectId(id)})    
        if not obj:
            raise NotFoundError(message=f"{self.type} with id {id} wasn't found.")
        return T(**obj)
    
    async def put(self, id: str, obj: T) -> T:
        updated_obj: UpdateResult = await self._collection.find_one_and_update({"_id":  ObjectId(id)}, {"$set": obj.model_dump()})
        if not updated_obj:
            raise NotFoundError(message=f"{self.type} with id {id} wasn't found.")
        return T(**updated_obj)    


    async def post(self, obj_data: T) -> T:
        obj: InsertOneResult = await self._collection.insert_one(obj_data.model_dump(exclude_unset=True))    
        if not obj:
            raise NotFoundError(message=f"{self.type} with id {id} wasn't found.")
        return T(**obj)
    
    async def delete(self, id: str) -> T:
        obj: T = await self.get(id)   
        await self._collection.delete_one({"_id": ObjectId(id)})
        return obj
