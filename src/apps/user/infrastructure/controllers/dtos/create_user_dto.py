from pydantic import BaseModel
from ....domain.user import RoleEnum


class CreateUserDto(BaseModel):
    first_name: str
    last_name: str
    identification_number: int
    role: RoleEnum