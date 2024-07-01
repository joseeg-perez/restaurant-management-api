class Notification():
    def __init__(self, _id: str, user: str, body: str) -> None:
        self._id = _id
        self.user = user
        self.body = body