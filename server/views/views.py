from fastapi_restful import Api

from bl.controllers.controller import Controller
from bl.models.todo import Todo
from dal.todo_db_handler import TodoDBHandler
from .resources import TodoApi
from logger import logger


def initialize_api_resources(api: Api):

    db_handler = TodoDBHandler(type_str="todo", logger=logger)
    todo_controller = Controller[Todo](db_handler)
    todo_api = TodoApi(controller=todo_controller, logger=logger)
    
    api.add_resource(todo_api, "/todo/{id}", "/todo")
