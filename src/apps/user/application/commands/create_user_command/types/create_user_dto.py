from .....domain.user import RoleEnum

class CreateUserDto():
    username: str
    password: str
    identification_number: int
    role: RoleEnum