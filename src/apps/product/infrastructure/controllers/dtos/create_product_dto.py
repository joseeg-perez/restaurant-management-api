from pydantic import BaseModel

class CreateProductDto(BaseModel):
    name: str
    price: str
    stock: int