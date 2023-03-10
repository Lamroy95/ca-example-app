from dataclasses import dataclass
from uuid import UUID


@dataclass
class Task:
    id: UUID


class TaskResult:
    is_ready: bool
    location: str
