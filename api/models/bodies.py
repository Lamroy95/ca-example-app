from pydantic import BaseModel


class UrlEmote(BaseModel):
    url: str


class FileEmote(BaseModel):
    file: bytes
