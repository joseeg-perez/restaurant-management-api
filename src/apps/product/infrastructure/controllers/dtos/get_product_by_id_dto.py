from pydantic import BaseModel

class GetProductByIdDto(BaseModel):
    product_id: str