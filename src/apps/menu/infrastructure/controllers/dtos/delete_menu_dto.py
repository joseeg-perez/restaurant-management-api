from pydantic import BaseModel

class DeleteMenuDto(BaseModel):
    menu_id: str