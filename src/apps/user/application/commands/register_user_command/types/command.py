from .....domain.user import RoleEnum

class RegisterUserCommand():
    username: str
    password: str
    identification_number: int
    role: RoleEnum