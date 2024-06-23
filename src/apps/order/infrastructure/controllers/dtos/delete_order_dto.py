from pydantic import BaseModel

class DeleteOrderDto(BaseModel):
    order_id: str