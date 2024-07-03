from fastapi import APIRouter 
from ....auth.application.commands.login import LoginService
from ...application.commands import CreateUserService, RegisterUserService
from ...application.queries import GetAllUsersService
from .dtos import CreateUserDto, RegisterUserDto, LoginDto
from ..repositories import PostgreUserRepository
from ..models import UserModel

router = APIRouter(tags=['User'])
user_model = UserModel
repository = PostgreUserRepository(user_model)

@router.get("/user")
def get_all_users():
    service = GetAllUsersService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.post('/user')
def create_user(user: CreateUserDto):
    service = CreateUserService(repository)
    response = service.execute(user)

    return response.unwrap()

@router.post('/user/register')
def register_user(registerDto: RegisterUserDto):
    service = RegisterUserService(repository)
    response = service.execute(registerDto)

    return response.unwrap()

@router.post('/users/login')
def login_user(loginDto: LoginDto):
    service = LoginService(repository)
    response = service.execute(loginDto)

    return response.unwrap()