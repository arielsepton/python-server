from fastapi import status
from fastapi_restful import Resource
from fastapi.responses import JSONResponse
from bl.controllers.controller import Controller

from bl.models.todo import Todo
from bl.schemas.todo import TodoSchema



class TodoApi(Resource):
    def __init__(self):
        self.controller: Controller = Controller[Todo](type_str="todo")
    
    async def get(self, id: str):
        todo: Todo = await self.controller.get(id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=todo.model_dump())

    async def post(self, todo_schema: TodoSchema):
        todo: Todo = Todo(**todo_schema)
        created_todo: Todo = await self.controller.post(todo)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_todo.model_dump(exclude_unset=True))
    
    async def delete(self, id: str):
        deleted_todo: Todo = await self.controller.delete(id)
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=deleted_todo.model_dump())
    
    async def put(self, id: str, todo_schema: TodoSchema):
        updated_todo: Todo = await self.controller.put(id, todo_schema)
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=updated_todo.model_dump())
