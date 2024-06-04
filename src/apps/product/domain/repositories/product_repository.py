from abc import ABC, abstractmethod 

class ProductRepository(ABC):
    @abstractmethod
    def find_all_products(self):
        pass

    @abstractmethod
    def find_product_by_id(self, id: int):
        pass

    @abstractmethod
    def save_product(self, product):
        pass

    @abstractmethod
    def delete_product(self, id: int):
        pass

    @abstractmethod
    def update_product(self, product):
        pass