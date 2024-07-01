from abc import ABC, abstractmethod 
from ..dish import Dish

class DishRepository(ABC):
    @abstractmethod
    def find_all_dishes(self):
        pass

    @abstractmethod
    def find_dish_by_id(self, id: str):
        pass

    @abstractmethod
    def save_dish(self, dish: Dish, menu_id: str):
        pass

    @abstractmethod
    def delete_dish(self, dish: Dish):
        pass

    @abstractmethod
    def update_dish(self, dish: Dish):
        pass