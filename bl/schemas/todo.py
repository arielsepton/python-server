from pydantic import BaseModel


class TodoSchema(BaseModel):
    todo_name: str
    reminder: str
    responsible: str
