from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TaskIdResponse(BaseModel):
    task_id: UUID


class TaskResultResponse(BaseModel):
    is_ready: bool
    content: Optional[bytes]
