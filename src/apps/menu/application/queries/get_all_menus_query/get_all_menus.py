from typing import List
from ....domain import Menu, MenuRepository
from ...exceptions import NoMenuFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllMenusService(Service[None, List[Menu]]):

    def __init__(self, menu_repository: MenuRepository) -> None:
        super().__init__()
        self.menu_repository = menu_repository

    def execute(self) -> Result[List[Menu]]:
        menus = self.menu_repository.find_all_menus()
        if (len(menus) == 0):
            return Result[List[Menu]].make_failure(error=NoMenuFoundException())
        
        return Result[List[Menu]].make_success(value=menus)