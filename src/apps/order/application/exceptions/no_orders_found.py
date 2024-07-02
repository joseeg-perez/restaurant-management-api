from core.application.exceptions.application_exception import ApplicationException

class NoOrderFoundException(ApplicationException):
    def __init__(self, message='No orders found'):
        self.message = message
        super().__init__(self.message)