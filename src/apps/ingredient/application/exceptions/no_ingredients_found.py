from core.application.exceptions.application_exception import ApplicationException

class NoIngredientFoundException(ApplicationException):
    def __init__(self, message='No ingredients found'):
        self.message = message
        super().__init__(self.message)