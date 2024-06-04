from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer(), primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    price = Column(Float())
    stock = Column(Integer())
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.name