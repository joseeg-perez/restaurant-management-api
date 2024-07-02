from pydantic import BaseModel
from ....domain.order import StatusEnum

class CreateOrderDto(BaseModel):
    owner_id: str
    menu_id: str
    dish_id: str
    order_price: float
    order_status: StatusEnum
