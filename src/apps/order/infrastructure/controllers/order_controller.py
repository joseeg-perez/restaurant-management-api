from fastapi import APIRouter, status, HTTPException

from apps.notification.application.commands.create_notification_command.create_notification import CreateNotificationService
from apps.notification.infrastructure.models.postgre_notification_model import NotificationModel
from ....notification.infrastructure.repositories.postgre_notification_repository import PostgreNotificationRepository
from ...application.commands import CreateOrderService

from ...application.queries import GetAllOrdersService
from .dtos import CreateOrderDto
from ..repositories import PostgreOrderRepository
from ..models import OrderModel

from ....auth.infrastructure.middlewares.verify_token_route import VerifyTokenRoute

router = APIRouter(route_class=VerifyTokenRoute, tags=['Orders'])
order_model = OrderModel
notification_model = NotificationModel
notification_repository = PostgreNotificationRepository(notification_model)
repository = PostgreOrderRepository(order_model)

@router.get("/orders")
def get_all_orders():
    service = GetAllOrdersService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.post('/orders')
def create_order(order: CreateOrderDto):
    service = CreateOrderService(repository)
    notification_service = CreateNotificationService(notification_repository)
    service.subscribe(notification_service)
    response = service.execute(order)

    return response.unwrap()