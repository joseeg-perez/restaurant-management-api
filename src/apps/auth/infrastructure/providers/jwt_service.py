from fastapi.responses import JSONResponse
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from apps.user.infrastructure.models.postgre_user_model import UserModel

class JwtService():
    
    def expire_date(days: int):
        date = datetime.now()
        new_date = date + timedelta(days)
        return new_date
    
    def generateToken(self, user: UserModel) -> str:
        token =  encode(payload = {**user, "exp": self.expire_date(1)}, key=getenv("SECRET_KEY"), algorithm="HS256")
        return token
    
    def validateToken(self, token: str, output: False):
        try:
            if output:
                return decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
            decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
        except exceptions.DecodeError:
            return JSONResponse(status_code=401, content={"error": "Unauthorized"})
        except exceptions.ExpiredSignatureError:
            return JSONResponse(status_code=400, content={"error": "Token expired"})