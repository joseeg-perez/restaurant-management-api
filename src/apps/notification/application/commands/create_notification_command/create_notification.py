from apps.notification.application.repositories.notification_repository import NotificationRepository
from core.application.events.subscriber import Subscriber
from ....application.entities.notification import Notification
from .types import CreateNotificationDto
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateNotificationService(Service[CreateNotificationDto, str], Subscriber[CreateNotificationDto]):

    def __init__(self, notification_repository: NotificationRepository) -> None:
        super().__init__()
        self.notification_repository = notification_repository
        self.idGenerator = UUIDService

    def update(self, data: CreateNotificationDto):
        data = CreateNotificationDto(**data)
        self.execute(data)

    def execute(self, data: CreateNotificationDto) -> Result[str]:
        id = self.idGenerator.generate_id()
        notification = Notification(id, data.user_id, data.body)
        self.notification_repository.save_notification(notification)

        return Result[str].make_success(value=id)