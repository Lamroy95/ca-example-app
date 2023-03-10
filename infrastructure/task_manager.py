from emotes.interfaces.task_manager import TaskManager
from emotes.models.dto.task import TaskResult, Task


class TaskManagerImpl(TaskManager):
    def __init__(self):
        super().__init__()
