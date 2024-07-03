from core.application.exceptions.application_exception import ApplicationException

class UserNotFoundException(ApplicationException):
    def __init__(self, message='User not found'):
        self.message = message
        super().__init__(self.message)