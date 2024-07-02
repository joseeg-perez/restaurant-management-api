from typing import List

from apps.user.application.queries.get_all_users_query.get_all_users import GetAllUsersService
from core.application.events.publisher import Publisher
from ....domain import Ingredient, IngredientRepository
from ...exceptions import IncompleteIngredientListException
from .types.get_ingredients_list_dto import GetIngredientsListDto, CreateNotificationDto
from core.application.services.application_service import Service
from core.application.results.result import Result

from ..get_all_ingredients_query.get_all_ingredients import GetAllIngredientService

class GetIngredientsListService(Service[GetIngredientsListDto, Ingredient], Publisher[CreateNotificationDto]):

    def __init__(self, ingredient_repository: IngredientRepository, get_all_users: GetAllUsersService) -> None:
        super().__init__()
        self.ingredient_repository = ingredient_repository
        self.get_all_users = get_all_users


    def execute(self, data: GetIngredientsListDto) -> Result[List[Ingredient]]:        
        ingredients_list = GetAllIngredientService(self.ingredient_repository).execute().unwrap()
        filtered_ingredients = []

        for ingredient_id in data:
            for ingredient_saved in ingredients_list:
                if ingredient_id == ingredient_saved.entity_id and ingredient_saved.quantity > 0:
                    ingredient_saved.quantity-= 1
                    ingredient = Ingredient(ingredient_saved.entity_id, ingredient_saved.name, ingredient_saved.quantity)
                    filtered_ingredients.append(ingredient)

        if(len(filtered_ingredients) != len(data)):
            users = self.get_all_users
            filtered_users = [user for user in users if user.role == 'admin'] 
            for admin in filtered_users:
                notification = {'user_id': admin.entity_id, 'body': f'Hello {admin.username}, we need to do a re-stock. Please, check the ingredients list.'}
                self.notify(notification)
            return Result[Ingredient].make_failure(error=IncompleteIngredientListException())

        self.ingredient_repository.update_ingredient(filtered_ingredients)
        return Result[List[Ingredient]].make_success(value=filtered_ingredients)