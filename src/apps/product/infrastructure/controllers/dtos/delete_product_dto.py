from pydantic import BaseModel

class DeleteProductDto(BaseModel):
    product_id: str