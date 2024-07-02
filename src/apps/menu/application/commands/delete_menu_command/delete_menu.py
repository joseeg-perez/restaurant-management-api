from ....domain import MenuRepository
from ...exceptions import NoMenuFoundException
from .types import DeleteMenuDto
from core.application.services.application_service import Service
from core.application.results.result import Result

class DeleteMenuService(Service[DeleteMenuDto, str]):

    def __init__(self, menu_repository: MenuRepository) -> None:
        super().__init__()
        self.menu_repository = menu_repository

    def execute(self, data: DeleteMenuDto) -> Result[str]:        
        menu = self.menu_repository.find_menu_by_id(data.menu_id)
        if (menu is None):
            return Result[str].make_failure(error=NoMenuFoundException())  

        self.menu_repository.delete_menu(menu) 

        return Result[str].make_success(value=menu.entity_id)