from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class OrderModel(Base):
    __tablename__ = 'Order'

    id_client = Column(String(), primary_key=True)
    id_menu = Column(String(), primary_key=True)
    id_dish = Column(String(), primary_key=True)
    price = Column(Float(), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.__tablename__