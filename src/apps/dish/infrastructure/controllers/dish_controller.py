from fastapi import APIRouter, status, HTTPException

from apps.notification.application.commands.create_notification_command.create_notification import CreateNotificationService
from apps.notification.infrastructure.models.postgre_notification_model import NotificationModel
from apps.notification.infrastructure.repositories.postgre_notification_repository import PostgreNotificationRepository
from apps.user.application.queries.get_all_users_query.get_all_users import GetAllUsersService
from apps.user.domain.repositories.user_repository import UserRepository
from apps.user.infrastructure.models.postgre_user_model import UserModel
from apps.user.infrastructure.repositories.postgre_user_repository import PostgreUserRepository    
from ...application.commands import CreateDishService, DeleteDishService
from ...application.queries import GetDishByIdService, GetAllDishesService
from .dtos import CreateDishDto, GetDishByIdDto, DeleteDishDto
from ..repositories import PostgreDishRepository
from ..models import DishModel

from ....ingredient.application.queries.get_ingredients_list_query.get_ingredients_list import GetIngredientsListService
from ....ingredient.infrastructure.repositories.postgre_ingredient_repository import PostgreIngredientRepository
from ....ingredient.infrastructure.models import Ingredient as IngredientModel


router = APIRouter(tags=['Dishes'])
dish_model = DishModel
repository = PostgreDishRepository(dish_model)

notification_model = NotificationModel
ingredient_model = IngredientModel
user_model = UserModel

notification_repository = PostgreNotificationRepository(notification_model)
ingredient_repository = PostgreIngredientRepository(ingredient_model)
user_repository = PostgreUserRepository(user_model)

@router.get("/dishes")
def get_all_dishes():
    service = GetAllDishesService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.get('/dish/{id}')
def get_dish_by_id(id: str):
    service = GetDishByIdService(repository)
    response = service.execute(GetDishByIdDto(dish_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)

    return response.unwrap()

@router.post('/dishes')
def create_dish(dish: CreateDishDto):
    get_all_users = GetAllUsersService(user_repository).execute().unwrap()
    notification_service = CreateNotificationService(notification_repository)
    get_all_ingredients = GetIngredientsListService(ingredient_repository, get_all_users)
    get_all_ingredients.subscribe(notification_service)

    service = CreateDishService(repository, get_all_ingredients)
    response = service.execute(dish)

    return response.unwrap()

@router.delete('/dish/{id}')
def delete_dish(id: str):
    service = DeleteDishService(repository)
    response = service.execute(DeleteDishDto(dish_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)
    
    return response.unwrap()