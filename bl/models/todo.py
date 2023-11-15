from typing import Optional
from pydantic import BaseModel, Field
from .pyobject_id import PyObjectId


class Todo(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    todo_name: str
    reminder: str
    responsible: str

    @property
    def parsed_id(self) -> str:
        return str(self.id) if self.id else None