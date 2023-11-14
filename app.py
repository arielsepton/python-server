from fastapi import FastAPI
from fastapi_restful import Api
from server.exceptions import not_found_exception_handler, conflict_exception_handler
from common import ConflictError, NotFoundError
import uvicorn

from server.views import initialize_api_resources


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(exception_handlers={
        NotFoundError: not_found_exception_handler,
        ConflictError: conflict_exception_handler
    })

    api: Api = Api(app)

    initialize_api_resources(api)
    return app


main = create_app()

if __name__ == "__name__":
    uvicorn.run(main, host="0.0.0.0", port=8000, reload=True)