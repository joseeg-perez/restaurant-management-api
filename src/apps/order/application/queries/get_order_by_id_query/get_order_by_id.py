from ....domain import Order, OrderRepository
from ...exceptions import NoOrderFoundException
from .types import GetOrderByIdDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetOrderByIdService(Service[GetOrderByIdDto, Order]):

    def __init__(self, order_repository: OrderRepository) -> None:
        super().__init__()
        self.order_repository = order_repository

    def execute(self, data: GetOrderByIdDto) -> Result[Order]:        
        order = self.order_repository.find_order_by_id(data.order_id)
        if (order is None):
            return Result[Order].make_failure(error=NoOrderFoundException())   

        return Result[Order].make_success(value=order)