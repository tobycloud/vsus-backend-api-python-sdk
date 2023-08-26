from backend_api.api import get_api
from backend_api.user import User
from backend_api.workspace import Workspace


class Instance:
    id: str
    owner: str
    workspace: str

    def __init__(self, *, id: str = "", owner: str = "", workspace: str = "") -> None:
        self.id = id
        self.owner = owner
        self.workspace = workspace

    def __repr__(self) -> str:
        return f"Instance(id={self.id}, owner={self.owner}, workspace={self.workspace})"

    def __str__(self) -> str:
        return self.id

    @staticmethod
    async def get(id: str) -> "Instance":
        """
        Fetch an instance.
        """

        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        instance = api.pocketbase.collection("instances").get_one(id)

        return Instance(
            id=instance.id, owner=instance.owner, workspace=instance.workspace  # type: ignore
        )

    @staticmethod
    async def new(user: User, workspace: Workspace) -> "Instance" | None:
        """
        Create a new instance.
        """

        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        async with api.session.get(
            f"{api.url}/new/{workspace.id}/instance",
            params={"owner": user.id},
            timeout=60,
        ) as response:
            result = await response.json()

            return Instance(
                id=result["id"], owner=result["owner"], workspace=result["workspace"]
            )

    async def delete(self) -> None:
        """
        Delete an instance.
        """

        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        async with api.session.delete(
            f"{api.url}/workspace/{self.id}",
            timeout=60,
        ) as response:
            await response.json()
