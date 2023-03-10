from emotes.interfaces.task_manager import TaskManager
from infrastructure.task_manager import TaskManagerImpl


def task_manager_provider() -> TaskManager:
    return TaskManagerImpl()
