from core.domain.entity.domain_entity import DomainEntity
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "admin"
    CHEF = "chef"
    WAITER = "waiter"
    CLIENT = "client"

class User(DomainEntity[str]):
    def __init__(self, _id: str, first_name: str, last_name: str, identification_number: int, role: RoleEnum) -> None:
        super().__init__(_id)
        self.first_name = first_name
        self.last_name = last_name
        self.identification_number = identification_number
        self.role = role