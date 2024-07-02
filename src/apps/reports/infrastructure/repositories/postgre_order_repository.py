from typing import List, Tuple
from sqlalchemy import func
from ...application.repositories.order_repository import OrderRepository
from core.infrastructure.db_session.postgre_session import Session
from ....order.infrastructure.models.postgre_order_model import OrderModel
from ....menu.infrastructure.models.postgre_menu_model import MenuModel
from ....dish.infrastructure.models.postgre_dish_model import DishModel

class PostgreOrderRepository(OrderRepository):
    
    def __init__(self, order_model: OrderModel, menu_model: MenuModel, dish_model: DishModel):
        self.order_model = order_model
        self.menu_model = menu_model
        self.dish_model = dish_model
        self.session = Session()
        
    def get_orders_by_menu(self) -> List[Tuple[str, str, str, str]]:
        try:
            result = (self.session.query(self.menu_model.name, self.dish_model.name, self.order_model.price, self.order_model.status)
                    .join(self.menu_model, self.order_model.id_menu == self.menu_model.entity_id)
                    .join(self.dish_model, self.order_model.id_dish == self.dish_model.entity_id).all())
            
            orders = [{"menu_name": menu_name, "dish_name": dish_name, "price": price, "status": status} for menu_name, dish_name, price, status in result]
            return orders
        
        except Exception as e:
            raise Exception(e.__str__())
        
        
    def get_total_sales_from_orders_by_dish(self) -> List[Tuple[str, str]]:
        try:
            result = (self.session.query(
                self.dish_model.name, func.sum(self.order_model.price).label('total_sales')
            )
            .join(self.dish_model, self.order_model.id_dish == self.dish_model.entity_id)
            .group_by(self.dish_model.name)
            .all())
            
            total_sales = [{"dish_name": dish_name, "total_sales": total_sales} for dish_name, total_sales in result]
            return total_sales
        
        except Exception as e:
            raise Exception(e.__str__())
        