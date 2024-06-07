from pydantic import BaseModel

class DeleteIngredientDto(BaseModel):
    ingredient_id: str