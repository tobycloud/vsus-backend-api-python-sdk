from aiohttp import ClientSession

global api_instance


class API:
    url: str
    session: ClientSession

    def __init__(self, url: str, session: ClientSession = ClientSession()) -> None:
        self.url = url
        self.session = session

        global api_instance
        api_instance = self

    async def close(self) -> None:
        await self.session.close()


api_instance: API | None = None


def get_api() -> API | None:
    return api_instance
