from pydantic import BaseModel

class CreateNotificationDto(BaseModel):
    user_id: str
    body: str