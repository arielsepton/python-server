from fastapi import status
from fastapi_restful import Resource
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from bl.controllers.controller import Controller

from bl.models.todo import Todo
from bl.schemas.todo import TodoSchema
from logging import Logger


class TodoApi(Resource):
    def __init__(self, controller: Controller[Todo], logger: Logger):
        self.controller: Controller = controller
        self._logger: Logger = logger

    async def get(self, id: str, request: Request):
        todo: Todo = await self.controller.get(id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=todo.model_dump())

    async def post(self, todo_schema: TodoSchema, request: Request):
        todo: Todo = Todo(todo_name=todo_schema.todo_name, reminder=todo_schema.reminder, responsible=todo_schema.responsible)
        created_todo: Todo = await self.controller.post(todo)
        return JSONResponse(status_code=status.HTTP_200_OK, content=created_todo.model_dump(exclude_unset=True))
    
    async def delete(self, id: str, request: Request):
        deleted_todo: Todo = await self.controller.delete(id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=deleted_todo.model_dump())
    
    async def put(self, id: str, todo_schema: TodoSchema, request: Request):
        updated_todo: Todo = await self.controller.put(id, todo_schema)
        return JSONResponse(status_code=status.HTTP_200_OK, content=updated_todo.model_dump())
