from ....domain import Product, ProductRepository
from ...exceptions import NoProductFoundException
from .types import DeleteProductDto
from core.application.services.application_service import ApplicationService
from core.application.results.result import Result

class DeleteProductService(ApplicationService[DeleteProductDto, str]):

    def __init__(self, product_repository: ProductRepository) -> None:
        super().__init__()
        self.product_repository = product_repository

    def execute(self, data: DeleteProductDto) -> Result[str]:        
        product = self.product_repository.find_product_by_id(data.product_id)
        if (product is None):
            return Result[str].make_failure(error=NoProductFoundException())  

        self.product_repository.delete_product(product) 

        return Result[str].make_success(value=product.aggregate_id)