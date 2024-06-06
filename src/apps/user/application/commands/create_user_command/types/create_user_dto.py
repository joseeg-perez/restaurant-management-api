from .....domain.user import RoleEnum

class CreateUserDto():
    first_name: str
    last_name: str
    identification_number: int
    role: RoleEnum