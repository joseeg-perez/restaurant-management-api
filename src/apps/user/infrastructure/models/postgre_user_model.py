from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class UserModel(Base):
    __tablename__ = 'User'

    entity_id = Column(String(), primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    identification_number = Column(Integer(), nullable=False, unique=True)
    role = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())