from ...application.entities.notification import Notification
from ...application.repositories.notification_repository import NotificationRepository
from ..models import NotificationModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreNotificationRepository(NotificationRepository):
    
    def __init__(self, notification_model):
        self.notification_model = notification_model
        self.session = Session()

    def find_all_notifications(self):
        notifications = self.session.query(self.notification_model).all()
        
        return notifications

    def save_notification(self, notification: Notification):        
        user = NotificationModel(
            notification_id=notification._id,
            id_client=notification.user,
            body=notification.body
        )

        try: 
            self.session.add(user)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())
