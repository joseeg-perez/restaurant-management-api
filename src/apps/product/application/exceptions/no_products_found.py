from core.application.exceptions.application_exception import ApplicationException

class NoProductFoundException(ApplicationException):
    def __init__(self, message):
        self.message = 'No products found'
        super().__init__(self.message)