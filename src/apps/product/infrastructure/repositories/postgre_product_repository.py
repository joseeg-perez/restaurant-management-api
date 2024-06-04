from ...domain.repositories.product_repository import ProductRepository
from core.infrastructure.db_session.postgre_session import Session

class PostgreProductRepository(ProductRepository):
    
    def __init__(self, product_model):
        self.product_model = product_model
        self.session = Session()

    def find_all_products(self):
        products = self.session.query(self.product_model).all()
        return products

    def find_product_by_id(self, id: int):
        pass

    def save_product(self, product):
        pass

    def delete_product(self, id: int):
        pass

    def update_product(self, product):
        pass


   