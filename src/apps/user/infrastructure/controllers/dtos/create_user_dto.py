from pydantic import BaseModel
from ....domain.user import RoleEnum

class CreateUserDto(BaseModel):
    username: str
    password: str
    identification_number: int
    role: RoleEnum