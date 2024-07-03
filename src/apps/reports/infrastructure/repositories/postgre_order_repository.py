from typing import List, Tuple
from sqlalchemy import func
from ...application.repositories.order_repository import OrderRepository
from core.infrastructure.db_session.postgre_session import Session
from ....order.infrastructure.models.postgre_order_model import OrderModel
from ....menu.infrastructure.models.postgre_menu_model import MenuModel
from ....dish.infrastructure.models.postgre_dish_model import DishModel
from ....user.infrastructure.models.postgre_user_model import UserModel

class PostgreOrderRepository(OrderRepository):
    
    def __init__(self, order_model: OrderModel, menu_model: MenuModel, dish_model: DishModel, client_model: UserModel):
        self.order_model = order_model
        self.menu_model = menu_model
        self.dish_model = dish_model
        self.client_model = client_model
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


    def get_frequent_clients(self):
        try:
            query = self.session.query(
                self.client_model.username, 
                func.count(self.order_model.id_client).label('client_count')
            ).join(
                self.order_model, 
                self.order_model.id_client == self.client_model.entity_id
            ).group_by(
                self.client_model.username
            ).order_by(
                func.count(self.order_model.id_client).desc()
            )
            result = query.all()
            
            frequent_clients = [{"client_name": client_name, "client_count": client_count} for client_name,  client_count in result]
            return frequent_clients
        
        except Exception as e:
            raise Exception(e.__str__())


    def get_frequent_dishes(self):
        try:
            query = self.session.query(
                self.dish_model.name, 
                func.count(self.order_model.id_dish).label('dish_count')
            ).join(
                self.order_model, 
                self.order_model.id_dish == self.dish_model.entity_id
            ).group_by(
                self.dish_model.name
            ).order_by(
                func.count(self.order_model.id_dish).desc()
            )
            result = query.all()
            
            frequent_dishes = [{"dish_name": dish_name, "dish_count": dish_count} for dish_name,  dish_count in result]
            return frequent_dishes
        
        except Exception as e:
            raise Exception(e.__str__())
        