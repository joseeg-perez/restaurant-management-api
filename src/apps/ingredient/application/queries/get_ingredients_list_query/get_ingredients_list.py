from typing import List
from ....domain import Ingredient, IngredientRepository
from ...exceptions import IncompleteIngredientListException
from .types.get_ingredients_list_dto import GetIngredientsListDto
from core.application.services.application_service import Service
from core.application.results.result import Result

from ..get_all_ingredients_query.get_all_ingredients import GetAllIngredientService

class GetIngredientsListService(Service[GetIngredientsListDto, Ingredient]):

    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository

    def execute(self, data: GetIngredientsListDto) -> Result[List[Ingredient]]:        
        ingredients_list = GetAllIngredientService(self.ingredient_repository).execute().unwrap()
        filtered_ingredients = []
        for ingredient in ingredients_list:
            if ingredient.entity_id in data and ingredient.quantity > 0:
                ingredient.quantity-= 1
                filtered_ingredients.append(ingredient)

        if(len(filtered_ingredients) < len(data)):
            #TODO: notify observer
            return Result[Ingredient].make_failure(error=IncompleteIngredientListException())

        self.ingredient_repository.update_ingredient(filtered_ingredients)
        return Result[List[Ingredient]].make_success(value=filtered_ingredients)