from core.application.exceptions.application_exception import ApplicationException

class InvalidPasswordException(ApplicationException):
    def __init__(self, message='Invalid password'):
        self.message = message
        super().__init__(self.message)