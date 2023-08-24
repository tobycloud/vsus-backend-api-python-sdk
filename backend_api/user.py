from backend_api.api import get_api


class User:
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def __repr__(self) -> str:
        return f"User(id={self.id})"

    def __str__(self) -> str:
        return self.id

    @staticmethod
    async def fetch(id: str) -> "User" | None:
        """
        Fetch a user from the API.
        """
        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        async with api.session.get(
            f"{api.url}/api/collections/users/records/{id}",
            timeout=60,
        ) as response:
            if response.status != 200:
                return None
            return User(id)
