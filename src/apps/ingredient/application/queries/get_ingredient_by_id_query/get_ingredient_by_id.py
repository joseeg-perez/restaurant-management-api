from ....domain import Ingredient, IngredientRepository
from ...exceptions import NoIngredientFoundException
from .types import GetIngredientByIdDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetIngredientByIdService(Service[GetIngredientByIdDto, Ingredient]):

    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository

    def execute(self, data: GetIngredientByIdDto) -> Result[Ingredient]:        
        ingredient = self.ingredient_repository.find_ingredient_by_id(data.ingredient_id)
        
        if (ingredient is None):
            return Result[Ingredient].make_failure(error=NoIngredientFoundException())   

        return Result[Ingredient].make_success(value=ingredient)