from typing import List
from ....domain import Dish, DishRepository
from ...exceptions import NoDishFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllDishesService(Service[None, List[Dish]]):

    def __init__(self, menu_repository: DishRepository) -> None:
        super().__init__()
        self.menu_repository = menu_repository

    def execute(self) -> Result[List[Dish]]:
        dishes = self.menu_repository.find_all_dishes()
        if (len(dishes) == 0):
            return Result[List[Dish]].make_failure(error=NoDishFoundException())
        
        return Result[List[Dish]].make_success(value=dishes)