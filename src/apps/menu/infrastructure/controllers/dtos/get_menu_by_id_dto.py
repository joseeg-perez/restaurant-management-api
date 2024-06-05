from pydantic import BaseModel

class GetMenuByIdDto(BaseModel):
    menu_id: str