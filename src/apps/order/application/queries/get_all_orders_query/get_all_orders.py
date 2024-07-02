from typing import List
from ....domain import Order, OrderRepository
from ...exceptions import NoOrderFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllOrdersService(Service[None, List[Order]]):

    def __init__(self, order_repository: OrderRepository) -> None:
        super().__init__()
        self.order_repository = order_repository

    def execute(self) -> Result[List[Order]]:
        orders = self.order_repository.find_all_orders()
        if (len(orders) == 0):
            return Result[List[Order]].make_failure(error=NoOrderFoundException())
        
        return Result[List[Order]].make_success(value=orders)