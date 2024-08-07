from datetime import datetime
from ...domain import User, UserRepository
from ..models import UserModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreUserRepository(UserRepository):
    
    def __init__(self, user_model):
        self.user_model = user_model
        self.session = Session()

    def find_all_users(self):
        users = self.session.query(self.user_model).all()
        
        return users

    def find_user_by_username(self, username: str):
        user = self.session.query(self.user_model).filter_by(username=username).first()
        
        return user

    def save_user(self, user: User):        
        user = UserModel(
            entity_id=user._id,
            username=user.username,
            password=user.password,
            identification_number=user.identification_number,
            role=user.role.value,
            created_at=datetime.now(),
        )

        try: 
            self.session.add(user)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())
