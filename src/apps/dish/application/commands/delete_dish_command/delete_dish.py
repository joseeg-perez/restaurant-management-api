from ....domain import DishRepository
from ...exceptions import NoDishFoundException
from .types import DeleteDishDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class DeleteDishService(Service[DeleteDishDto, str]):

    def __init__(self, dish_repository: DishRepository) -> None:
        super().__init__()
        self.dish_repository = dish_repository

    def execute(self, data: DeleteDishDto) -> Result[str]:        
        dish = self.dish_repository.find_dish_by_id(data.dish_id)
        if (dish is None):
            return Result[str].make_failure(error=NoDishFoundException())  

        self.dish_repository.delete_dish(dish) 

        return Result[str].make_success(value=dish.aggregate_id)