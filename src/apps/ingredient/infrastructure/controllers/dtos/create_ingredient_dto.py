from pydantic import BaseModel

class CreateIngredientDto(BaseModel):
    name: str
    availability: int
    unit: str