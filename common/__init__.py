from .exceptions.exceptions import ConflictError, NotFoundError, InternalError

# shared_types
from pydantic import BaseModel
from typing import TypeVar

T = TypeVar('T', bound=BaseModel)
