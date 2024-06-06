from pydantic import BaseModel

class GetDishByIdDto(BaseModel):   
    dish_id: str