from abc import ABC, abstractmethod 
from ..menu import Menu

class MenuRepository(ABC):
    @abstractmethod
    def find_all_menus(self):
        pass

    @abstractmethod
    def find_menu_by_id(self, id: str):
        pass

    @abstractmethod
    def save_menu(self, menu: Menu):
        pass

    @abstractmethod
    def delete_menu(self, menu: Menu):
        pass

    @abstractmethod
    def update_menu(self, menu: Menu):
        pass