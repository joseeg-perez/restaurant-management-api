from abc import ABC, abstractmethod 
from ..user import User

class UserRepository(ABC):
    @abstractmethod
    def find_all_users(self):
        pass

    @abstractmethod
    def save_user(self, user: User):
        pass

