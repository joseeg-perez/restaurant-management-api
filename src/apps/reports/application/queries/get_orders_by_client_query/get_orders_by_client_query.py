from typing import List
from ...repositories.order_repository import OrderRepository
from core.application.results.result import Result
from core.application.services.application_service import Service
from ...exceptions.no_orders_found import NoOrdersFoundException    

class GetOrdersByClientsService(Service):
    def __init__(self, order_repository: OrderRepository) -> None:
        super().__init__()
        self.order_repository = order_repository
        
    def execute(self) -> Result[List[str]]:
        orders = self.order_repository.get_orders_by_client()
        if (len(orders) == 0):
            return Result[List[str]].make_failure(error=NoOrdersFoundException())
    
        return Result[List[str]].make_success(value=orders)