from fastapi import APIRouter, status, HTTPException    
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

ingredient_model = IngredientModel
ingredient_repository = PostgreIngredientRepository(ingredient_model)

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
    get_all_ingredients = GetIngredientsListService(ingredient_repository)
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