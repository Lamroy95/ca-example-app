from pathlib import Path

from emotes.interfaces.reader import EmoteReader
from emotes.models.dto import Emote
from infrastructure.http_session import HTTPSession


class LocalFileReader(EmoteReader):
    async def read_emote(self, path: Path) -> Emote:
        content = path.read_bytes()
        return Emote(content)


class RemoteFileReader(EmoteReader):
    async def read_emote(self, path: str) -> Emote:
        async with HTTPSession() as session:
            content = await session.get_file(path)
            return Emote(content)


class MemoryFileReader(EmoteReader):
    async def read_emote(self, file: bytes) -> Emote:
        return Emote(file)
