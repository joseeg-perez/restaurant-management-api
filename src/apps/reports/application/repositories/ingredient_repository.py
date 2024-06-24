from abc import ABC, abstractmethod 

class IngredientRepository(ABC):
    @abstractmethod
    def get_ingredients_available_quantities(self):
        pass