from .....domain.order import StatusEnum

class CreateOrderDto():
    owner_id: str
    menu_id: str
    dish_id: str
    order_price: float
    order_status: StatusEnum

class CreateNotificationDto():
    user_id: str
    body: str