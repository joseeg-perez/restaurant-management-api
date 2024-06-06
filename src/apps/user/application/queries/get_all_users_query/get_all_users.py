from typing import List
from ....domain import User, UserRepository
from ...exceptions import NoUserFoundException
from core.application.services.application_service import Service
from core.application.results.result import Result

class GetAllUsersService(Service[None, List[User]]):

    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__()
        self.user_repository = user_repository

    def execute(self) -> Result[List[User]]:
        users = self.user_repository.find_all_users()
        if (len(users) == 0):
            return Result[List[User]].make_failure(error=NoUserFoundException())
        
        return Result[List[User]].make_success(value=users)