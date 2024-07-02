from typing import List

class GetIngredientsListDto():
    ingredients: List[str]

class CreateNotificationDto():
    user_id: str
    body: str