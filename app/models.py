from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclass
class Task:
    id: UUID
    name: str
    status: TaskStatus
    created_at: datetime
    result: str | None = None


def create_task(name: str) -> Task:
    return Task(
        id=uuid4(),
        name=name,
        status=TaskStatus.PENDING,
        created_at=datetime.now(),
    )