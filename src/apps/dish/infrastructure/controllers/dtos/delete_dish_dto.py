from pydantic import BaseModel

class DeleteDishDto(BaseModel):
    dish_id: str