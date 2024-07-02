from typing import List, Tuple
from ...repositories.ingredient_repository import IngredientRepository
from ...exceptions import NoIngredientFoundException
from core.application.results.result import Result
from core.application.services.application_service import Service

class GetAllIngredientWithQuantitiesService(Service[None, List[str]]):
    
    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository
        
    def execute(self) -> Result[List[Tuple[str, str]]]:
        ingredients = self.ingredient_repository.get_all_ingredients_with_quantities()
        if (len(ingredients) == 0):
            return Result[List[Tuple[str, str]]].make_failure(error=NoIngredientFoundException())
        
        return Result[List[Tuple[str, str]]].make_success(value=ingredients)