from abc import abstractmethod
from typing import List
from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from dal.db_handler_base import DbHandlerBase
from db_connection import db
from common import NotFoundError, InternalError, T
from logging import Logger


class MongoDbHandler(DbHandlerBase):
    def __init__(self, type_str: str, logger: Logger):
        self.type_str = type_str
        self._collection = db[f"{self.type_str}_collection"]
        self._logger: Logger = logger

    @abstractmethod
    def init(self, data: dict) -> T:
        pass
    
    async def get_all(self) -> List[T]:
        return [self.init(obj) async for obj in self._collection.find()]

    async def get(self, id: str) -> T:
        obj: dict = await self._collection.find_one({"_id": ObjectId(id)})
        
        if not obj:
            raise NotFoundError(message=f"{self.type_str} with id {id} wasn't found.")
        return self.init(obj)

    async def put(self, id: str, obj: T) -> T:
        updated_obj: UpdateResult = await self._collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": obj.model_dump()})
        
        if not updated_obj:
            raise NotFoundError(message=f"{self.type_str} with id {id} wasn't found.")
        return self.init(updated_obj)

    async def post(self, obj_data: T) -> T:
        inserted_obj: InsertOneResult = await self._collection.insert_one(obj_data.model_dump(exclude_unset=True))
        obj: dict = await self._collection.find_one({"_id": inserted_obj.inserted_id})
        
        if not obj:
            raise InternalError(message=f"{self.type_str} creation did not succeed.")
        return self.init(obj)

    async def delete(self, id: str) -> T:
        obj: T = await self.get(id)
        await self._collection.delete_one({"_id": ObjectId(id)})

        self._logger.info(f"{self.type_str} with id {id} was deleted successfully.")
        return obj
