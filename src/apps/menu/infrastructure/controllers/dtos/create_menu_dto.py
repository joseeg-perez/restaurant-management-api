from pydantic import BaseModel

class CreateMenuDto(BaseModel):
    name: str