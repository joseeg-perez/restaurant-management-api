from core.application.exceptions.application_exception import ApplicationException

class NoDishFoundException(ApplicationException):
    def __init__(self, message='No dishes found'):
        self.message = message
        super().__init__(self.message)