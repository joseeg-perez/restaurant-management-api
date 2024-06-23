from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class OrderModel(Base):
    __tablename__ = 'Client_Order'

    pg_id_user = Column(Integer(), primary_key=True)
    pg_id_menu = Column(Integer(), primary_key=True)
    pg_id_dish = Column(Integer(), primary_key=True)
    aggregate_id = Column(String(), nullable=False, unique=True)
    price = Column(Float(), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.name