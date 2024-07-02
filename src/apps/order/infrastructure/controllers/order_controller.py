from fastapi import APIRouter, status, HTTPException

from apps.notification.application.commands.create_notification_command.create_notification import CreateNotificationService
from apps.notification.infrastructure.models.postgre_notification_model import NotificationModel
from ....notification.infrastructure.repositories.postgre_notification_repository import PostgreNotificationRepository
from ...application.commands import CreateOrderService, DeleteOrderService

from ...application.queries import GetAllOrdersService, GetOrderByIdService
from .dtos import CreateOrderDto, GetOrderByIdDto, DeleteOrderDto
from ..repositories import PostgreOrderRepository
from ..models import OrderModel

router = APIRouter(tags=['Orders'])
order_model = OrderModel
notification_model = NotificationModel
notification_repository = PostgreNotificationRepository(notification_model)
repository = PostgreOrderRepository(order_model)

@router.get("/orders")
def get_all_orders():
    service = GetAllOrdersService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.get('/order/{id}')
def get_order_by_id(id: str):
    service = GetOrderByIdService(repository)
    response = service.execute(GetOrderByIdDto(order_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)

    return response.unwrap()

@router.post('/orders')
def create_order(order: CreateOrderDto):
    service = CreateOrderService(repository)
    notification_service = CreateNotificationService(notification_repository)
    service.subscribe(notification_service)
    response = service.execute(order)

    return response.unwrap()

@router.delete('/order/{id}')
def delete_order(id: str):
    service = DeleteOrderService(repository)
    response = service.execute(DeleteOrderDto(order_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)
    
    return response.unwrap()