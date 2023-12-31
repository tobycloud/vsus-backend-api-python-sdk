from backend_api.workspace import Workspace as Workspace

class Instance:
    id: str
    owner: str
    workspace: str
    def __init__(
        self, *, id: str = ..., owner: str = ..., workspace: str = ...
    ) -> None: ...
    def toJson(self) -> dict: ...
    @staticmethod
    async def get(id: str) -> Instance: ...
    @staticmethod
    async def new(workspace: Workspace) -> Instance: ...
    @staticmethod
    async def inject_ssh_key(id: str, key: str) -> None: ...
    @staticmethod
    async def delete(workspace: Workspace, id: str) -> None: ...
