from bl.models.todo import Todo
from dal.mongo_db_handler import MongoDbHandler


class TodoDBHandler(MongoDbHandler):
    def init(self, data: dict) -> Todo:
        return Todo(**data)
