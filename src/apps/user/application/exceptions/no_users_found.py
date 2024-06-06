from core.application.exceptions.application_exception import ApplicationException

class NoUserFoundException(ApplicationException):
    def __init__(self, message='No users found'):
        self.message = message
        super().__init__(self.message)