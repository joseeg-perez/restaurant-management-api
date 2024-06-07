from fastapi import APIRouter, status, HTTPException    
from ...application.commands import CreateIngredientService, DeleteIngredientService
from ...application.queries import GetAllIngredientService, GetIngredientByIdService
from .dtos import CreateIngredientDto, DeleteIngredientDto, GetIngredientByIdDto
from ..repositories import PostgreIngredientRepository
from ..models import Ingredient

router = APIRouter(tags=['Ingredients'])
ingredient_model = Ingredient
repository = PostgreIngredientRepository(ingredient_model)

@router.get("/ingredients")
def get_all_ingredients():
    service = GetAllIngredientService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.get('/ingredient/{id}')
def get_ingredient_by_id(id: str):
    service = GetIngredientByIdService(repository)
    response = service.execute(GetIngredientByIdDto(ingredient_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)

    return response.unwrap()

@router.post('/ingredient')
def create_ingredient(ingredient: CreateIngredientDto):
    service = CreateIngredientService(repository)
    response = service.execute(ingredient)

    return response.unwrap()

@router.delete('/ingredient/{id}')
def delete_ingredient(id: str):
    service = DeleteIngredientService(repository)
    response = service.execute(DeleteIngredientDto(ingredient_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)
    
    return response.unwrap()