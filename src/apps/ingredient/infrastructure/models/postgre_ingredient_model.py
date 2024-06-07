from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class Ingredient(Base):
    __tablename__ = 'Ingredient'

    pg_id_ingredient = Column(Integer(), primary_key=True)
    aggregate_id = Column(String(), nullable=False, unique=True)
    name = Column(String(25), nullable=False, unique=True)
    availability = Column(Integer(), nullable=False)
    unit = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.name