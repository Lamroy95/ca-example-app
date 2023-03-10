from uuid import UUID

from fastapi import Depends, APIRouter
from fastapi.params import Path

from api.dependencies.reader import local_reader_provider, remote_reader_provider, memory_reader_provider
from api.dependencies.task_manager import task_manager_provider
from api.models.bodies import UrlEmote, FileEmote
from api.models.responses import TaskIdResponse, TaskResultResponse
from emotes.interfaces.reader import EmoteReader
from emotes.interfaces.task_manager import TaskManager
from emotes.services.convert import convert_webp_emote_from_path, convert_webp_emote_from_file


async def convert_webp_emote_url(
        emote: UrlEmote,
        task_manager: TaskManager = Depends(task_manager_provider),
        reader: EmoteReader = Depends(remote_reader_provider)
) -> TaskIdResponse:
    """
    Convert WEBP emote from url
    """
    task = convert_webp_emote_from_path(emote.url, reader, task_manager)
    return TaskIdResponse(task_id=task.id)


async def convert_webp_emote_file(
        emote: FileEmote,
        task_manager: TaskManager = Depends(task_manager_provider),
        reader: EmoteReader = Depends(memory_reader_provider)
) -> TaskIdResponse:
    """
    Convert WEBP emote from file
    """
    task = convert_webp_emote_from_file(emote.file, reader, task_manager)
    return TaskIdResponse(task_id=task.id)


async def check_task_result(
        task_id: UUID = Path(alias="task_id"),
        task_manager: TaskManager = Depends(task_manager_provider),
        reader: EmoteReader = Depends(local_reader_provider)
) -> TaskResultResponse:
    """
    Get task result. If task is done, content field will be present
    """
    result = task_manager.get_result(task_id)
    if result.is_ready:
        content = reader.read_emote(result.location)
    else:
        content = None

    return TaskResultResponse(is_ready=result.is_ready, content=content)


def setup(router: APIRouter):
    router.add_api_route("/emotes/convert/webp/url", convert_webp_emote_url, methods=["POST"])
    router.add_api_route("/emotes/convert/webp/file", convert_webp_emote_file, methods=["POST"])
    router.add_api_route("/emotes/check_result/{task_id}", check_task_result, methods=["GET"])
