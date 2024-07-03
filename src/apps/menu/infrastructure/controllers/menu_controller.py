from fastapi import APIRouter, status, HTTPException    
from ...application.commands import CreateMenuService, DeleteMenuService
from ...application.queries import GetMenuByIdService, GetAllMenusService
from .dtos import CreateMenuDto, GetMenuByIdDto, DeleteMenuDto
from ..repositories import PostgreMenuRepository
from ..models import MenuModel

from ....auth.infrastructure.middlewares.verify_token_route import VerifyTokenRoute

router = APIRouter(route_class=VerifyTokenRoute, tags=['Menus'])
menu_model = MenuModel
repository = PostgreMenuRepository(menu_model)

@router.get("/menus")
def get_all_menus():
    service = GetAllMenusService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.get('/menu/{id}')
def get_menu_by_id(id: str):
    service = GetMenuByIdService(repository)
    response = service.execute(GetMenuByIdDto(menu_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)

    return response.unwrap()

@router.post('/menus')
def create_menu(menu: CreateMenuDto):
    service = CreateMenuService(repository)
    response = service.execute(menu)

    return response.unwrap()

@router.delete('/menu/{id}')
def delete_menu(id: str):
    service = DeleteMenuService(repository)
    response = service.execute(DeleteMenuDto(menu_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)
    
    return response.unwrap()