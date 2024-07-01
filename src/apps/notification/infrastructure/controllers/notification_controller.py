from fastapi import APIRouter 
from ...application.commands import CreateNotificationService
from ...application.queries import GetAllNotificationsService
from .dtos import CreateNotificationDto
from ..repositories import PostgreNotificationRepository
from ..models import NotificationModel

router = APIRouter(tags=['Notifications'])
notification_model = NotificationModel
repository = PostgreNotificationRepository(notification_model)

@router.get("/notifications")
def get_all_users():
    service = GetAllNotificationsService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.post('/notification')
def create_user(user: CreateNotificationDto):
    service = CreateNotificationService(repository)
    response = service.execute(user)

    return response.unwrap()

