from ....domain import Menu, MenuRepository
from ...exceptions import NoMenuFoundException
from .types import GetMenuByIdDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetMenuByIdService(Service[GetMenuByIdDto, Menu]):

    def __init__(self, menu_repository: MenuRepository) -> None:
        super().__init__()
        self.menu_repository = menu_repository

    def execute(self, data: GetMenuByIdDto) -> Result[Menu]:        
        menu = self.menu_repository.find_menu_by_id(data.menu_id)
        if (menu is None):
            return Result[Menu].make_failure(error=NoMenuFoundException())   

        return Result[Menu].make_success(value=menu)