from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class MenuModel(Base):
    __tablename__ = 'Menu'

    pg_id_menu = Column(Integer(), primary_key=True)
    aggregate_id = Column(String(), nullable=False, unique=True)
    name = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.name