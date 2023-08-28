from backend_api.api import get_api
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

    def toJson(self) -> dict:
        return {"id": self.id, "owner": self.owner, "workspace": self.workspace}

    def __str__(self) -> str:
        return str(self.toJson())

    @staticmethod
    async def get(id: str) -> "Instance":
        """
        Fetch an instance.
        """

        api = get_api()

        instance = api.pocketbase.collection("instances").get_one(id)

        return Instance(
            id=instance.id, owner=instance.owner, workspace=instance.workspace  # type: ignore
        )

    @staticmethod
    async def new(workspace: Workspace) -> "Instance":
        """
        Create a new instance.
        """

        api = get_api()

        async with api.session.get(
            f"{api.url}/new/{workspace.id}/instance",
            params={"owner": workspace.owner},
            timeout=60,
        ) as response:
            result = await response.json()

            return Instance(
                id=result["id"], owner=result["owner"], workspace=result["workspace"]
            )

    @staticmethod
    async def put(id: str, key: str) -> None:
        """
        Put an instance.
        """

        api = get_api()

        await api.session.put(
            f"{api.url}/instance/{id}/set-ssh-key",
            data={"key": key},
            timeout=60,
        )

    @staticmethod
    async def delete(workspace: Workspace, id: str) -> None:
        """
        Delete an instance.
        """

        api = get_api()

        await api.session.delete(
            f"{api.url}/workspace/{workspace.id}/instance/{id}",
            timeout=60,
        )
