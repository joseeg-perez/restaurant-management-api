from abc import ABC, abstractmethod 
from ..user import User

class UserRepository(ABC):
    @abstractmethod
    def find_all_users(self):
        pass

    def find_user_by_username(self, username: str):
        pass

    @abstractmethod
    def save_user(self, user: User):
        pass

