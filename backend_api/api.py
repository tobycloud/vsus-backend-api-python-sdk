from aiohttp import ClientSession
from pocketbase import PocketBase

global api_instance


class API:
    url: str
    session: ClientSession
    pocketbase: PocketBase

    def __init__(
        self,
        url: str,
        session: ClientSession = ClientSession(),
        pocketbase: PocketBase | None = None,
    ) -> None:
        self.url = url
        self.session = session

        if not pocketbase:
            raise RuntimeError("PocketBase is not initialized")

        self.pocketbase = pocketbase

        global api_instance
        api_instance = self

    async def close(self) -> None:
        await self.session.close()


api_instance: API | None = None


def get_api() -> API | None:
    return api_instance
