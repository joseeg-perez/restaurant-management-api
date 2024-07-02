from core.application.exceptions.application_exception import ApplicationException

class NoNotificationFoundException(ApplicationException):
    def __init__(self, message='No notifications found'):
        self.message = message
        super().__init__(self.message)