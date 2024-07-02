class CreateNotificationDto():
    def __init__(self, user_id: str, body: str) -> None:
        self.user_id = user_id
        self.body = body