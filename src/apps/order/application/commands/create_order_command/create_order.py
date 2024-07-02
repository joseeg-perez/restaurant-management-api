from ....domain import Order, OrderRepository
from .types import CreateOrderDto, CreateNotificationDto
from .....notification.application.commands.create_notification_command.types.create_notification_dto import CreateNotificationDto
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService
from core.application.events.publisher import Publisher

class CreateOrderService(Service[CreateOrderDto, str], Publisher[CreateNotificationDto]):

    def __init__(self, order_repository: OrderRepository) -> None:
        super().__init__()
        self.order_repository = order_repository
        self.idGenerator = UUIDService
        self.subscribers = []

    def execute(self, data: CreateOrderDto) -> Result[str]:
        id = self.idGenerator.generate_id()
        order = Order(id, data.owner_id, data.menu_id, data.dish_id, data.order_price, data.order_status)
        self.order_repository.save_order(order)
        
        notification = {'user_id': data.owner_id, 'body': f'The order is in staus {data.order_status}'}
        self.notify(notification)

        return Result[str].make_success(value=id)