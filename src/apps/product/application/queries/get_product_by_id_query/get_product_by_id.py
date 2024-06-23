from ....domain import Product, ProductRepository
from ...exceptions import NoProductFoundException
from .types import GetProductByIdDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetProductByIdService(Service[GetProductByIdDto, Product]):

    def __init__(self, product_repository: ProductRepository) -> None:
        super().__init__()
        self.product_repository = product_repository

    def execute(self, data: GetProductByIdDto) -> Result[Product]:        
        product = self.product_repository.find_product_by_id(data.product_id)
        print('ESTE ES EL RODUCTO::: ',product)
        
        if (product is None):
            return Result[Product].make_failure(error=NoProductFoundException())   

        return Result[Product].make_success(value=product)