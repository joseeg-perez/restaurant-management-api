from ...domain import Dish, DishRepository
from ..models import DishModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreDishRepository(DishRepository):
    
    def __init__(self, dish_model):
        self.dish_model = dish_model
        self.session = Session()

    def find_all_dishes(self):
        dishes = self.session.query(self.dish_model).all()
        
        return dishes

    def find_dish_by_id(self, id: str):
        dish = self.session.query(self.dish_model).filter_by(aggregate_id=id).first()

        return dish

    def save_dish(self, dish: Dish):   
        dish = DishModel(
            aggregate_id=dish._id,
            name=dish.name,
            description=dish.description,
            price=dish.price,
            disponibility=dish.disponibility
        )

        try: 
            self.session.add(dish)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())

    def delete_dish(self, dish: Dish):
        try:
            self.session.delete(dish)
            self.session.commit()
        except Exception as e:
            raise Exception(e.__str__())

    def update_dish(self, dish: Dish):
        pass