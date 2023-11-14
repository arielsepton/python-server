from pydantic import BaseModel, Field
from datetime import datetime


class TodoSchema(BaseModel):
    name: str
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    reminder: str
    responsible: str
