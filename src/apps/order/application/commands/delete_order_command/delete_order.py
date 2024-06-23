from ....domain import OrderRepository
from ...exceptions import NoOrderFoundException
from .types import DeleteOrderDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class DeleteOrderService(Service[DeleteOrderDto, str]):

    def __init__(self, order_repository: OrderRepository) -> None:
        super().__init__()
        self.order_repository = order_repository

    def execute(self, data: DeleteOrderDto) -> Result[str]:        
        order = self.order_repository.find_order_by_id(data.order_id)
        if (order is None):
            return Result[str].make_failure(error=NoOrderFoundException())  

        self.order_repository.delete_order(order) 

        return Result[str].make_success(value=order.aggregate_id)