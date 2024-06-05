from pydantic import BaseModel

class CreateProductDto(BaseModel):
    name: str
    price: float
    stock: int