from pocketbase.models.utils import BaseModel

from backend_api.api import get_api
from backend_api.user import User


class WorkspaceModel(BaseModel):
    owner: str
    instances: list[str]


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
    async def new(user: User) -> "Workspace":
        """
        Create a new workspace.
        """

        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

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

        if not api:
            raise RuntimeError("API is not initialized")

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

        if not api:
            raise RuntimeError("API is not initialized")

        api.pocketbase.collection("workspaces").delete(id)
