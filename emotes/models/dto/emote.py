from dataclasses import dataclass


@dataclass
class Emote:
    REQUIRED_SIZE = (100, 100)
    content: bytes
