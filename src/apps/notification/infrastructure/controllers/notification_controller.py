from fastapi import APIRouter 
from ...application.queries import GetAllNotificationsService
from ..repositories import PostgreNotificationRepository
from ..models import NotificationModel
from ....auth.infrastructure.middlewares.verify_token_route import VerifyTokenRoute

router = APIRouter(route_class=VerifyTokenRoute, tags=['Notifications'])
notification_model = NotificationModel
repository = PostgreNotificationRepository(notification_model)


@router.get("/notifications")
def get_all_users():
    service = GetAllNotificationsService(repository)
    response = service.execute()
    
    return response.unwrap()
