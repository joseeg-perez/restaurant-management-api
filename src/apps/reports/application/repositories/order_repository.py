from abc import ABC, abstractmethod 

class OrderRepository(ABC):
    @abstractmethod
    def get_orders_by_menu(self):
        pass
    
    def get_total_sales_from_orders_by_dish(self):
        pass

    def get_frequent_clients(self):
        pass
    
    def get_frequent_dishes(self):
        pass