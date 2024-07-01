from typing import List

class CreateDishDto():
    menu_id: str
    name: str
    ingredients: List[str]
    description: str
    price: float
    availability: bool