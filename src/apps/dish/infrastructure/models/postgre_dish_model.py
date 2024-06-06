from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class DishModel(Base):
    __tablename__ = 'Dish'

    pg_id_dish = Column(Integer(), primary_key=True)
    aggregate_id = Column(String(), nullable=False, unique=True)
    name = Column(String(20), nullable=False, unique=True)
    description = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)
    disponibility = Column(Boolean(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.name