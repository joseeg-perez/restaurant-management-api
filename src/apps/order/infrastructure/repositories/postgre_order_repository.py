from ...domain import Order, OrderRepository
from ..models import OrderModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreOrderRepository(OrderRepository):
    
    def __init__(self, order_model):
        self.order_model = order_model
        self.session = Session()

    def find_all_orders(self):
        orders = self.session.query(self.order_model).all()
        
        return orders

    def save_order(self, order: Order):        
        order = OrderModel(
            id_client=order.owner,
            id_menu=order.menu,
            id_dish=order.dish,
            price=order.price,
            status=order.status
        )

        try: 
            self.session.add(order)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())

    def update_order(self, order: Order):
        pass