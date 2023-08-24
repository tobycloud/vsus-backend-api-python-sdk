from backend_api.api import get_api
from backend_api.user import User


class Workspace:
    id: str
    owner: str
    instances: list[str]

    def __init__(
        self, *, id: str = "", owner: str = "", instances: list[str] = []
    ) -> None:
        self.id = id
        self.owner = owner
        self.instances = instances

    def __repr__(self) -> str:
        return (
            f"Workspace(id={self.id}, owner={self.owner}, instances={self.instances})"
        )

    def __str__(self) -> str:
        return self.id

    @staticmethod
    async def new(user: User) -> "Workspace" | None:
        """
        Create a new workspace.
        """

        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        async with api.session.get(
            f"{api.url}/new/workspace",
            params={"owner": user.id},
            timeout=60,
        ) as response:
            result = await response.json()

            return Workspace(
                id=result["id"], owner=result["owner"], instances=result["instances"]
            )
