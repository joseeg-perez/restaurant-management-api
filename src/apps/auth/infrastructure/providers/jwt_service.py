from fastapi.responses import JSONResponse
import jwt
from datetime import datetime, timedelta
from os import getenv

class JwtService():
    
    def generateToken(id: str ) -> str:
        date = datetime.now()
        new_date = date + timedelta(minutes=40)
        token =  jwt.encode(payload = {"id": id, "exp": new_date}, key=getenv("SECRET_KEY"), algorithm="HS256")
        return token
    
    def validateToken(token: str, output: False):
        try:
            if output:
                return jwt.decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
            jwt.decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
        except jwt.exceptions.DecodeError:
            return JSONResponse(status_code=401, content={"error": "Unauthorized"})
        except jwt.exceptions.ExpiredSignatureError:
            return JSONResponse(status_code=400, content={"error": "Token expired"})