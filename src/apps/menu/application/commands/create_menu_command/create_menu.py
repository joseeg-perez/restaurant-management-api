from ....domain import Menu, MenuRepository
from .types import CreateMenuDto
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateMenuService(Service[CreateMenuDto, str]):

    def __init__(self, menu_repository: MenuRepository) -> None:
        super().__init__()
        self.menu_repository = menu_repository
        self.idGenerator = UUIDService

    def execute(self, data: CreateMenuDto) -> Result[str]:
        id = self.idGenerator.generate_id()
        menu = Menu(id, data.name)
        self.menu_repository.save_menu(menu)

        return Result[str].make_success(value=id)