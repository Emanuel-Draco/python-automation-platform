from fastapi import APIRouter, HTTPException
from app.services.scheduler import schedule_task
from app.schemas.task import TaskCreate, TaskResponse
from app.services import task_service

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/tasks", response_model=TaskResponse)
def create_task(payload: TaskCreate):
    task = task_service.create_task(
        name=payload.name,
        task_type=payload.task_type,
        schedule=payload.schedule
    )
    return task.__dict__


@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    return [task.__dict__ for task in task_service.list_tasks()]


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: str):
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.__dict__


@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "deleted"}


@router.post("/tasks/{task_id}/schedule")
def schedule_task_endpoint(task_id: str):
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    schedule_task(task_id, seconds=10)

    return {
        "status": "scheduled",
        "task_id": task_id,
        "interval_seconds": 10
    }