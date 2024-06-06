from core.application.exceptions.application_exception import ApplicationException

class NoMenuFoundException(ApplicationException):
    def __init__(self, message='No menus found'):
        self.message = message
        super().__init__(self.message)