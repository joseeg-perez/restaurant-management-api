from ....domain import User, UserRepository
from .types import RegisterUserCommand
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService
from core.infrastructure.providers.bcrypt_service import BcryptService

class RegisterUserService(Service[RegisterUserCommand, str]):

    def __init__(self, user_repository: UserRepository, idGenerator) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.idGenerator = UUIDService
        self.bycriptService = BcryptService

    def execute(self, data: RegisterUserCommand) -> Result[str]:
        id = self.idGenerator.generate_id()
        password = self.bycriptService.encrypt_password(data.password)
        user = User(id, data.username, password, data.identification_number, data.role)
        self.user_repository.save_user(user)

        return Result[str].make_success(value=id)