from abc import ABC
from uuid import UUID

from emotes.models.dto.task import Task, TaskResult


class TaskManager(ABC):
    def __init__(self):
        raise NotImplementedError

    def create_task(self) -> Task:
        raise NotImplementedError

    def get_result(self, task_id: UUID) -> TaskResult:
        raise NotImplementedError
