import json

from aiohttp import ClientSession


class API:
    url: str
    session: ClientSession

    def __init__(self, url: str, session: ClientSession = ClientSession()) -> None:
        self.url = url
        self.session = session

    async def new_instance(self, user_id: str) -> str:
        """
        Create a new instance.
        """

        async with self.session.get(
            f"{self.url}/new/instance",
            params={"user_id": user_id},
            timeout=60,
        ) as response:
            return json.loads(await response.content.read())["instance"]["ID"]
