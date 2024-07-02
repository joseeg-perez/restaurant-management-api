from fastapi import Form
from fastapi.security import OAuth2PasswordBearer

#Este servicio puede no ser necesario
class OAuthService():
    def __init__(self, secret: str):
        self.secret = secret

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
