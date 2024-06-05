from ....domain import Product, ProductRepository
from .types import CreateProductDto
from core.application.services.application_service import ApplicationService
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateProductService(ApplicationService[CreateProductDto, str]):

    def __init__(self, product_repository: ProductRepository) -> None:
        super().__init__()
        self.product_repository = product_repository
        self.idGenerator = UUIDService

    def execute(self, data: CreateProductDto) -> Result[str]:
        _id = self.idGenerator.generate_id()
        product = Product(_id, data.name, data.price, data.stock)
        self.product_repository.save_product(product)

        return Result[str].make_success(value=_id)