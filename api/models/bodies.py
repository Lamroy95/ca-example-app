from pydantic import BaseModel


class UrlEmoteBody(BaseModel):
    emote_url: str
