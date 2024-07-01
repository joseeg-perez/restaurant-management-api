from abc import ABC, abstractmethod 
from ..ingredient import Ingredient

class IngredientRepository(ABC):
    @abstractmethod
    def find_all_ingredients(self):
        pass

    @abstractmethod
    def find_ingredient_by_id(self, id: str):
        pass

    @abstractmethod
    def get_ingredient_list(self, ingredients_ids: list):
        pass

    @abstractmethod
    def save_ingredient(self, ingredient: Ingredient):
        pass

    @abstractmethod
    def delete_ingredient(self, ingredient: Ingredient):
        pass

    @abstractmethod
    def update_ingredient(self, ingredient: Ingredient):
        pass