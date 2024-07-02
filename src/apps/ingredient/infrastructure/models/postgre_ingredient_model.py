from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class Ingredient(Base):
    __tablename__ = 'Ingredient'

    entity_id = Column(String(), primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    quantity = Column(Integer(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.__tablename__
    


