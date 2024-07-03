from ...domain import Dish, DishRepository
from ..models.postgre_dish_model import DishModel, MenuDishModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreDishRepository(DishRepository):
    
    def __init__(self, dish_model):
        self.dish_model = dish_model
        self.dish_quantity = 10
        self.session = Session()

    def find_all_dishes(self):
        dishes = self.session.query(self.dish_model).all()
        
        return dishes

    def find_dish_by_id(self, id: str):
        dish = self.session.query(self.dish_model).filter_by(entity_id=id).first()

        return dish

    def save_dish(self, dish: Dish, menu_id: str):   
        dish_entity = DishModel(
            entity_id=dish._id,
            name=dish.name,
            description=dish.description,
            price=dish.price,
            availability=dish.availability
        )

        dish_menu = MenuDishModel(
            id_dish = dish._id,
            id_menu = menu_id,
            quantity = self.dish_quantity
        )

        try: 
            self.session.add(dish_entity)
            self.session.commit()
            self.session.add(dish_menu)
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
