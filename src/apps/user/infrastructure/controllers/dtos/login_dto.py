from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated, Depends

class LoginDto():
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]