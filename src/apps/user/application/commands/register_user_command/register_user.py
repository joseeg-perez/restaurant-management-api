from ....domain import User, UserRepository
from .types import RegisterUserCommand
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService
from core.infrastructure.providers.crypto_service import CryptoService

class RegisterUserService(Service[RegisterUserCommand, str]):

    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.idGenerator = UUIDService
        self.cryptoService = CryptoService

    def execute(self, data: RegisterUserCommand) -> Result[str]:
        id = self.idGenerator.generate_id()
        password = self.cryptoService.encrypt_password(data.password)
        user = User(id, data.username, password, data.identification_number, data.role)
        self.user_repository.save_user(user)

        return Result[str].make_success(value=id)