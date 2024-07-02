from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from core.infrastructure.db_session.postgre_session import Session, Base

session = Session()

class DishModel(Base):
    __tablename__ = 'Dish'

    entity_id = Column(String(), primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    description = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)
    availability = Column(Boolean(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.__tablename__
    
class IngredientDish(Base):
    __tablename__ = 'Ingredient_Dish'

    id_dish = Column(String(), nullable=False, primary_key=True)
    id_ingredient = Column(String(), nullable=False, primary_key=True)
    quantity = Column(Integer(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.__tablename__

class MenuDishModel(Base):
    __tablename__ = 'Menu_Dish'

    id_dish = Column(String(), primary_key=True)
    id_menu = Column(String(), primary_key=True)
    quantity = Column(Integer(), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.__tablename__