from fastapi import APIRouter 
from ...application.commands import CreateUserService
from ...application.queries import GetAllUsersService
from .dtos import CreateUserDto
from ..repositories import PostgreUserRepository
from ..models import UserModel

router = APIRouter(tags=['Users'])
user_model = UserModel
repository = PostgreUserRepository(user_model)

@router.get("/users")
def get_all_users():
    service = GetAllUsersService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.post('/users')
def create_user(user: CreateUserDto):
    service = CreateUserService(repository)
    response = service.execute(user)

    return response.unwrap()

