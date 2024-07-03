from core.application.exceptions.application_exception import ApplicationException

class UnauthorizedException(ApplicationException):
    def __init__(self, message='Unauthorized'):
        self.message = message
        super().__init__(self.message)