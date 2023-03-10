from aiohttp import ClientSession


class HTTPSession:
    def __init__(self):
        self._session = ClientSession()

    async def __aenter__(self):
        await self._session.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._session.__aexit__(*args, **kwargs)

    async def get_file(self, path: str) -> bytes:
        res = await self._session.get(url=path)
        return await res.read()
