from fastapi import FastAPI
from fastapi_restful import Api
from server.exceptions import not_found_exception_handler, conflict_exception_handler
from common import ConflictError, NotFoundError

from server.views import initialize_api_resources


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(exception_handlers={
        NotFoundError: not_found_exception_handler,
        ConflictError: conflict_exception_handler
    })

    initialize_api_resources(Api(app))
    return app

