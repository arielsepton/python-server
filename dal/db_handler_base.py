from abc import ABC, abstractmethod
from typing import List
from common import T


class DbHandlerBase(ABC):
    @abstractmethod
    async def get_all(self) -> List[T]:
        pass
    
    @abstractmethod
    async def get(self, id: str) -> T:
        pass
    
    @abstractmethod
    async def post(self, obj_data: T) -> T:
        pass
    
    @abstractmethod
    async def put(self, id: str, obj_data: T) -> T:
        pass
    
    @abstractmethod
    async def delete(self, id: str) -> T:
        pass

