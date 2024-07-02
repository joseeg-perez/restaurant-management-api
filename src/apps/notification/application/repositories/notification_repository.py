from typing import List
from ..entities.notification import Notification
from abc import ABC, abstractmethod 

class NotificationRepository(ABC):
    @abstractmethod
    def find_all_notifications(self) -> List[Notification]:
        pass

    @abstractmethod
    def save_notification(self, notification: Notification):
        pass

