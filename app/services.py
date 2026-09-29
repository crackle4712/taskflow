from app.models import Task, create_task


def create_new_task(name: str) -> Task:
    return create_task(name)