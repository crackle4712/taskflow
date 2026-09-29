from fastapi import FastAPI
from app.services import create_new_task


app = FastAPI(title="TaskFlow")


@app.get("/")
def home():
    return {"message": "TaskFlow is running!"}


@app.post("/tasks")
def create_new_task_endpoint(name: str):
    task = create_new_task(name)

    return {
        "id": str(task.id),
        "name": task.name,
        "status": task.status.value,
        "created_at": task.created_at,
        "result": task.result,
    }