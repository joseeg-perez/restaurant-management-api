import bcrypt

class BcryptService():
    
    def encrypt_password(password: str) -> str:
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        return hashed_password

    def check_password(password: str, hashed_password: str) -> bool:
        print(password, hashed_password)
        # password_bytes = password.encode('utf-8')
        # password = bcrypt.hashpw(password_bytes, salt)

        password_bytes = password.encode('utf-8')
        # password_bytes = password.encode('utf-8')
        # hashed_password_bytes = hashed_password.encode('utf-8')

        if (bcrypt.checkpw(password_bytes, hashed_password)):
            return True
        else:
            return False