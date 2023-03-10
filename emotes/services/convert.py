from emotes.interfaces.reader import EmoteReader
from emotes.interfaces.task_manager import TaskManager
from emotes.models.dto.task import Task


def convert_webp_emote_from_path(emote_path: str, reader: EmoteReader, task_manager: TaskManager) -> Task:
    raise NotImplementedError

    # emote = reader.read_emote(emote_path)
    # task = task_manager.create_task(...)
    # return task


def convert_webp_emote_from_file(emote_file: bytes, reader: EmoteReader, task_manager: TaskManager) -> Task:
    raise NotImplementedError
