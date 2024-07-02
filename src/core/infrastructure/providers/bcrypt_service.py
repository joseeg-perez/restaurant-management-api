import bcrypt

class BcryptService():
    
    def __init__(self):
        self.salt = bcrypt.gensalt()

    def encrypt_password(self, password: str) -> str:
        return bcrypt.hashpw(password, self.salt)

    def check_password(self, password: str, hashed_password: str) -> bool:
        if bcrypt.checkpw(password, hashed_password):
            return True
        else:
            return False