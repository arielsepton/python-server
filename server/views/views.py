from fastapi_restful import Api
from .resources import TodoApi


def initialize_api_resources(api: Api):
    api.add_resource(TodoApi(), "/todo/{id}", "/todo")
