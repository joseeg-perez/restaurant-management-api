from core.domain.entity.domain_entity import DomainEntity
from enum import Enum

class StatusEnum(str, Enum):
    RECEIVED = "received"
    PREPARING = "preparing"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order(DomainEntity[str]):
    def __init__(self, _id: str, owner: str, menu: str, dish: str, price: float, status: StatusEnum) -> None:
        super().__init__(_id)
        self.owner = owner
        self.menu = menu
        self.dish = dish
        self.price = price
        self.status = status
 
