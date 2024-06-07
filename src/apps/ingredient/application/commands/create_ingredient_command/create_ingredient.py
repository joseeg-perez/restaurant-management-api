from ....domain import Ingredient, IngredientRepository
from .types import CreateIngredientDto
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateIngredientService(Service[CreateIngredientDto, str]):

    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository
        self.idGenerator = UUIDService

    def execute(self, data: CreateIngredientDto) -> Result[str]:
        _id = self.idGenerator.generate_id()
        ingredient = Ingredient(_id, data.name, data.availability, data.unit)
        self.ingredient_repository.save_ingredient(ingredient)

        return Result[str].make_success(value=_id)