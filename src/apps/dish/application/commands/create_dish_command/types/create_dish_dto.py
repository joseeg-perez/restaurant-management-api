from typing import List

class CreateDishDto():
    name: str
    ingredients: List[str]
    description: str
    price: float
    disponibility: bool