from core.application.exceptions.application_exception import ApplicationException

class NoProductFoundException(ApplicationException):
    def __init__(self, message='No products found'):
        self.message = message
        super().__init__(self.message)