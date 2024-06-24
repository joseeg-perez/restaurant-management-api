from typing import List
from ...repositories.ingredient_repository import IngredientRepository
from ...exceptions import NoIngredientFoundException
from core.application.results.result import Result
from core.application.services.application_service import Service

class GetIngredientAvailableQuantitiesService(Service[None, List[str]]):
    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository
        
    def execute(self) -> Result[List[str]]:
        ingredients = self.ingredient_repository.get_ingredients_available_quantities()
        if (len(ingredients) == 0):
            return Result[List[str]].make_failure(error=NoIngredientFoundException())
        
        return Result[List[str]].make_success(value=ingredients)