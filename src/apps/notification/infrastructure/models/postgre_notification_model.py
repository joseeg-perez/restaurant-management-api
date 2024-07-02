from datetime import datetime
from sqlalchemy import Column, String, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class NotificationModel(Base):
    __tablename__ = 'Notification'

    notification_id = Column(String(), primary_key=True)
    id_client = Column(String(), nullable=False, unique=True)
    body = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.__tablename__