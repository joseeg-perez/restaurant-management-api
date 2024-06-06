from pydantic import BaseModel
from typing import List

class CreateDishDto(BaseModel):
    name: str
    ingredients: List[str]
    description: str
    price: float
    disponibility: bool