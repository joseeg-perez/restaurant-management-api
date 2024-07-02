from ....domain import User, UserRepository
from .types import CreateUserDto
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateUserService(Service[CreateUserDto, str]):

    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.idGenerator = UUIDService

    def execute(self, data: CreateUserDto) -> Result[str]:
        id = self.idGenerator.generate_id()
        user = User(id, data.username, data.password, data.identification_number, data.role)
        self.user_repository.save_user(user)

        return Result[str].make_success(value=id)