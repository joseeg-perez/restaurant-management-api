from typing import List
from ....domain import Product, ProductRepository
from ...exceptions import NoProductFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllProductsService(Service[None, List[Product]]):

    def __init__(self, product_repository: ProductRepository) -> None:
        super().__init__()
        self.product_repository = product_repository

    def execute(self) -> Result[List[Product]]:
        products = self.product_repository.find_all_products()
        if (len(products) == 0):
            return Result[List[Product]].make_failure(error=NoProductFoundException())
        
        return Result[List[Product]].make_success(value=products)