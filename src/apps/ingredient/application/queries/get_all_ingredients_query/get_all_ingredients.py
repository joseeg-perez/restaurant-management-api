from typing import List
from ....domain import Ingredient, IngredientRepository
from ...exceptions import NoIngredientFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllIngredientService(Service[None, List[Ingredient]]):

    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository

    def execute(self) -> Result[List[Ingredient]]:
        ingredients = self.ingredient_repository.find_all_ingredients()
        if (len(ingredients) == 0):
            return Result[List[Ingredient]].make_failure(error=NoIngredientFoundException())
        
        return Result[List[Ingredient]].make_success(value=ingredients)