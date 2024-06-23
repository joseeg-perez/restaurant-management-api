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

    def find_order_by_id(self, id: str):
        order = self.session.query(self.order_model).filter_by(aggregate_id=id).first()

        return order

    def save_order(self, order: Order):        
        order = OrderModel(
            pg_id_user=order.owner,
            pg_id_menu=order.menu,
            pg_id_dish=order.dish,
            aggregate_id=order._id,
            price=order.price,
            status=order.status
        )

        try: 
            self.session.add(order)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())

    def delete_order(self, order: Order):
        try:
            self.session.delete(order)
            self.session.commit()
        except Exception as e:
            raise Exception(e.__str__())

    def update_order(self, order: Order):
        pass