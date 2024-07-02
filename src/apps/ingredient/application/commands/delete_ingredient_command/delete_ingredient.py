from ....domain import Ingredient, IngredientRepository
from ...exceptions import NoIngredientFoundException
from .types import DeleteIngredientDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class DeleteIngredientService(Service[DeleteIngredientDto, str]):

    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository

    def execute(self, data: DeleteIngredientDto) -> Result[str]:        
        ingredient = self.ingredient_repository.find_ingredient_by_id(data.ingredient_id)
        if (ingredient is None):
            return Result[str].make_failure(error=NoIngredientFoundException())  

        self.ingredient_repository.delete_ingredient(ingredient) 

        return Result[str].make_success(value=ingredient.entity_id)