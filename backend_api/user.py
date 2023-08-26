from backend_api.api import get_api


class User:
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def __repr__(self) -> str:
        return f"User(id={self.id})"

    def toJson(self) -> dict:
        return {"id": self.id}

    def __str__(self) -> str:
        return str(self.toJson())

    @staticmethod
    async def get(id: str) -> "User":
        """
        Fetch a user from the API.
        """
        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        user = api.pocketbase.collection("users").get_one(id)

        return User(id=user.id)
