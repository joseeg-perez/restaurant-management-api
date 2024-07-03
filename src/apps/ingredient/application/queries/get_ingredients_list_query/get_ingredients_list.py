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

    def notify_admins(self):
        users = self.get_all_users
        filtered_users = [user for user in users if user.role == 'admin']
        for admin in filtered_users:
            print(admin.username)
            notification = {
                'user_id': admin.entity_id,
                'body': f'Hello {admin.username}, we need to do a re-stock. Please, check the ingredients list.'
            }
            self.notify(notification)

    def execute(self, data: GetIngredientsListDto) -> Result[List[Ingredient]]:
        ingredients_list = GetAllIngredientService(self.ingredient_repository).execute().unwrap()
        ingredients_dict = {ingredient.entity_id: ingredient for ingredient in ingredients_list}
        filtered_ingredients = []

        for ingredient_id in data:
            ingredient_saved = ingredients_dict.get(ingredient_id)
            if ingredient_saved and ingredient_saved.quantity > 0:
                ingredient_saved.quantity -= 1
                filtered_ingredients.append(Ingredient(ingredient_saved.entity_id, ingredient_saved.name, ingredient_saved.quantity))
            else:
                self.notify_admins()
                return Result[Ingredient].make_failure(error=IncompleteIngredientListException())

        self.ingredient_repository.update_ingredient(filtered_ingredients)
        return Result[List[Ingredient]].make_success(value=filtered_ingredients)