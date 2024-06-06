from ....domain import Dish, DishRepository
from ...exceptions import NoDishFoundException
from .types import GetDishByIdDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetDishByIdService(Service[GetDishByIdDto, Dish]):

    def __init__(self, dish_repository: DishRepository) -> None:
        super().__init__()
        self.dish_repository = dish_repository

    def execute(self, data: GetDishByIdDto) -> Result[Dish]:        
        dish = self.dish_repository.find_dish_by_id(data.dish_id)
        if (dish is None):
            return Result[Dish].make_failure(error=NoDishFoundException())   

        return Result[Dish].make_success(value=dish)