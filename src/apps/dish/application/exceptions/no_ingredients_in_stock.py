from core.application.exceptions.application_exception import ApplicationException

class NoIngredientInStockException(ApplicationException):
    def __init__(self, message= 'No ingredients in stock'):
        self.message = message
        super().__init__(self.message)