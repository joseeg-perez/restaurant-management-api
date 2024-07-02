from abc import ABC, abstractmethod 

class OrderRepository(ABC):
    @abstractmethod
    def get_orders_by_client(self):
        pass
    
    @abstractmethod
    def get_orders_by_menu(self):
        pass
    
    @abstractmethod
    def get_orders_by_dish(self):
        pass
    
    @abstractmethod
    def get_orders_by_status_delivered(self):
        pass