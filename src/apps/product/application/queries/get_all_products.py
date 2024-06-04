from typing import List
from ...domain.product import Product
from ...domain.repositories.product_repository import ProductRepository
from ..exceptions.no_products_found import NoProductFoundException

from core.application.services.application_service import ApplicationService
from core.application.results.result import Result

class GetAllProductsFromInventory(ApplicationService[None, List[Product]]):

    def __init__(self, product_repository: ProductRepository) -> None:
        super().__init__()
        self.product_repository = product_repository

    def execute(self) -> Result[List[Product]]:
        products = self.product_repository.find_all_products()
        if (len(products) == 0):
            return Result.make_failure(NoProductFoundException())

        return Result.make_success(products)