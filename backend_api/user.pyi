class User:
    id: str
    def __init__(self, id: str) -> None: ...
    def toJson(self) -> dict: ...
    @staticmethod
    async def get(id: str) -> User: ...
