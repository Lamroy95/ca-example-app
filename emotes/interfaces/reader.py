from abc import ABC

from emotes.models.dto import Emote


class EmoteReader(ABC):
    async def read_emote(self, path: str) -> Emote:
        raise NotImplementedError
