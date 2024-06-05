from abc import ABC, abstractmethod 
from ..product import Product

class ProductRepository(ABC):
    @abstractmethod
    def find_all_products(self):
        pass

    @abstractmethod
    def find_product_by_id(self, id: str):
        pass

    @abstractmethod
    def save_product(self, product: Product):
        pass

    @abstractmethod
    def delete_product(self, product: Product):
        pass

    @abstractmethod
    def update_product(self, product: Product):
        pass