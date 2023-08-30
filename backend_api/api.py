from aiohttp import ClientSession
from pocketbase import PocketBase

global api_instance


class API:
    url: str
    session: ClientSession
    pocketbase: PocketBase

    def __init__(self) -> None:
        ...

    async def init(
        self,
        url: str,
        session: ClientSession = ClientSession(),
        pocketbase: PocketBase = PocketBase(),
    ) -> None:
        self.url = url
        self.session = session
        self.pocketbase = pocketbase

        global api_instance
        api_instance = self

    async def close(self) -> None:
        await self.session.close()


api_instance: API | None = None


def get_api() -> API:
    if not api_instance:
        raise RuntimeError("API is not initialized")
    return api_instance
