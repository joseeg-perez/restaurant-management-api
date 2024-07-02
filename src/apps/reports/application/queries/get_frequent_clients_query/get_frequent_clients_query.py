from typing import List, Tuple
from ...repositories.order_repository import OrderRepository
from ...exceptions.no_orders_found import NoOrdersFoundException
from core.application.results.result import Result
from core.application.services.application_service import Service

class GetFrequentClientsService(Service[None, List[str]]):
    
    def __init__(self, order_repository: OrderRepository) -> None:
        super().__init__()
        self.order_repository = order_repository
        
    def execute(self) -> Result[List[Tuple[str, str]]]:
        clients = self.order_repository.get_frequent_clients()
        if (len(clients) == 0):
            return Result[List[Tuple[str, str]]].make_failure(error=NoOrdersFoundException())
    
        return Result[List[Tuple[str, str]]].make_success(value=clients)