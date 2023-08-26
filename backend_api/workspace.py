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

    def toJson(self) -> dict:
        return {"id": self.id, "owner": self.owner, "instances": self.instances}

    def __str__(self) -> str:
        return str(self.toJson())

    @staticmethod
    async def new(user: User) -> "Workspace":
        """
        Create a new workspace.
        """

        api = get_api()

        workspace = api.pocketbase.collection("workspaces").create({"owner": user.id})

        return Workspace(
            id=workspace.id, owner=workspace.owner, instances=workspace.instances  # type: ignore
        )

    @staticmethod
    async def get(id: str) -> "Workspace":
        """
        Fetch a workspace.
        """

        api = get_api()

        workspace = api.pocketbase.collection("workspaces").get_one(id)

        return Workspace(
            id=workspace.id, owner=workspace.owner, instances=workspace.instances  # type: ignore
        )

    @staticmethod
    async def delete(id: str) -> None:
        """
        Delete a workspace.
        """

        api = get_api()

        api.pocketbase.collection("workspaces").delete(id)
