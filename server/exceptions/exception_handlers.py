from fastapi import Request, status
from common import ConflictError, NotFoundError, InternalError
from fastapi.responses import JSONResponse


async def conflict_exception_handler(request: Request, exception: ConflictError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content=exception.message)

async def not_found_exception_handler(request: Request, exception: NotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=exception.message)

async def internal_exception_handler(request: Request, exception: InternalError):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=exception.message)
