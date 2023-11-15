from bl.models.todo import Todo
from dal.db_handler import DbHandler


class TodoDBHandler(DbHandler):
    async def init(self, data: dict) -> Todo:
        return Todo(**data)
