import json

from backend_api.api import get_api


class Workspace:
    id: str
    owner: str
    instances: list[str]

    def __init__(self, id: str, owner: str, instances: list[str]) -> None:
        self.id = id
        self.owner = owner
        self.instances = instances

    def __repr__(self) -> str:
        return (
            f"Workspace(id={self.id}, owner={self.owner}, instances={self.instances})"
        )

    def __str__(self) -> str:
        return self.id

    async def new(self, user_id: str) -> str:
        """
        Create a new workspace.
        """

        api = get_api()

        if not api:
            raise RuntimeError("API is not initialized")

        async with api.session.get(
            f"{api.url}/new/workspace",
            params={"user_id": user_id},
            timeout=60,
        ) as response:
            return json.loads(await response.content.read())["workspace"]["ID"]
