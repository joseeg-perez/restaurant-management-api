from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class UserModel(Base):
    __tablename__ = 'User'

    pg_id_user = Column(Integer(), primary_key=True)
    aggregate_id = Column(String(), nullable=False, unique=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    identification_number = Column(Integer(), nullable=False, unique=True)
    role = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())