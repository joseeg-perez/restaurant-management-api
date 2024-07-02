from abc import ABC, abstractmethod 
from ..order import Order

class OrderRepository(ABC):
    @abstractmethod
    def find_all_orders(self):
        pass

    @abstractmethod
    def find_order_by_id(self, id: str):
        pass

    @abstractmethod
    def save_order(self, order: Order):
        pass

    @abstractmethod
    def delete_order(self, order: Order):
        pass

    @abstractmethod
    def update_order(self, order: Order):
        pass