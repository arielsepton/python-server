class CustomError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class ConflictError(CustomError):
    pass

class AuthorizationError(CustomError):
    pass

class NotFoundError(CustomError):
    pass
