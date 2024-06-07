from pydantic import BaseModel

class GetIngredientByIdDto(BaseModel):
    ingredient_id: str