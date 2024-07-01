from typing import List
from apps.notification.application.repositories.notification_repository import NotificationRepository
from ...entities.notification import Notification
from ...exceptions import NoNotificationFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllNotificationsService(Service[None, List[Notification]]):

    def __init__(self, notification_repository: NotificationRepository) -> None:
        super().__init__()
        self.notification_repository = notification_repository

    def execute(self) -> Result[List[Notification]]:
        Notifications = self.notification_repository.find_all_notifications()
        if (len(Notifications) == 0):
            return Result[List[Notification]].make_failure(error=NoNotificationFoundException())
        
        return Result[List[Notification]].make_success(value=Notifications)