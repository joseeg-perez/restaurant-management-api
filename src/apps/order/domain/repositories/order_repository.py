from abc import ABC, abstractmethod 
from ..order import Order

class OrderRepository(ABC):
    @abstractmethod
    def find_all_orders(self):
        pass

    @abstractmethod
    def save_order(self, order: Order):
        pass

    @abstractmethod
    def update_order(self, order: Order):
        pass