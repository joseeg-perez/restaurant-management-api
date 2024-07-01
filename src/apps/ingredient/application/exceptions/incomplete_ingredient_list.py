from core.application.exceptions.application_exception import ApplicationException

class IncompleteIngredientListException(ApplicationException):
    def __init__(self, message='Ingredient list incomplete'):
        self.message = message
        super().__init__(self.message)