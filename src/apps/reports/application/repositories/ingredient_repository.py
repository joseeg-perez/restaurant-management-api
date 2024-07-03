from abc import ABC, abstractmethod 

class IngredientRepository(ABC):
    @abstractmethod
    def get_all_ingredients_with_quantities(self):
        pass