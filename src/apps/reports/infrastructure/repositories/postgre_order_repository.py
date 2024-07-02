from ...application.repositories.order_repository import OrderRepository
from core.infrastructure.db_session.postgre_session import Session

class PostgreOrderRepository(OrderRepository):
    
    def __init__(self, order_model):
        self.order_model = order_model
        self.session = Session()
        
    def get_orders_by_client(self):
        orders = self.session.execute('')
    
    def get_orders_by_menu(self):
        pass
    
    def get_orders_by_dish(self):
        pass
    
    def get_orders_by_status_delivered(self):
        pass