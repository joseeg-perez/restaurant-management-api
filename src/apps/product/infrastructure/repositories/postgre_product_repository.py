from ...domain import Product, ProductRepository
from ..models import Product as ProductModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreProductRepository(ProductRepository):
    
    def __init__(self, product_model):
        self.product_model = product_model
        self.session = Session()

    def find_all_products(self):
        products = self.session.query(self.product_model).all()
        
        return products

    def find_product_by_id(self, id: str):
        product = self.session.query(self.product_model).filter_by(aggregate_id=id).first()

        return product

    def save_product(self, product: Product):
        product = ProductModel(
            name=product._name,
            price=product._price,
            stock=product.stock,
            aggregate_id=product._id
        )

        try: 
            self.session.add(product)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())

    def delete_product(self, product: Product):
        try:
            self.session.delete(product)
            self.session.commit()
        except Exception as e:
            raise Exception(e.__str__())

    def update_product(self, product: Product):
        pass