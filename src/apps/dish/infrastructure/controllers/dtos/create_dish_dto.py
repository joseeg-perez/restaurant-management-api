from pydantic import BaseModel
from typing import List

class CreateDishDto(BaseModel):
    menu_id: str
    name: str
    ingredients: List[str]
    description: str
    price: float
    availability: bool