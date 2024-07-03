from .....user.domain import UserRepository
from typing import Dict
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.bcrypt_service import BcryptService
from auth.infrastructure.providers.jwt_service import JwtService
from .types import LoginCommand
from ...exceptions import UserNotFoundException, InvalidPasswordException

class LoginService(Service[LoginCommand, str]):
    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.bycriptService = BcryptService
        self.jwtService = JwtService

    def execute(self, data: LoginCommand) -> Result[Dict[str, str]]:
        user = self.user_repository.find_user_by_username(data.username)
        print('Esta es la password del suuario: ',user.password)
        if user is None:
            return Result[Dict[str, str]].make_failure(error=UserNotFoundException())
        if not self.bycriptService.check_password(data.password, user.password):
            return Result[Dict[str, str]].make_failure(error=InvalidPasswordException())
        return Result[Dict[str, str]].make_success({
            "token": self.jwtService.generate_token(user.id),
            "id": user.id
        })