from sqlalchemy.orm import Session
from app.models.task import Task, TaskDB
from app.db.session import SessionLocal
from uuid import uuid4


def get_db() -> Session:
    return SessionLocal()


def create_task(
    name: str,
    task_type: str,
    schedule: str,
    filename: str | None,
    interval_seconds: int,
) -> TaskDB:
    db = get_db()
    task = TaskDB(
        id=str(uuid4()),
        name=name,
        task_type=task_type,
        schedule=schedule,
        filename=filename,
        interval_seconds=interval_seconds,
        status="pending",
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task


def list_tasks() -> list[TaskDB]:
    db = get_db()
    tasks = db.query(TaskDB).all()
    db.close()
    return tasks


def get_task(task_id: str) -> TaskDB | None:
    db = get_db()
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    db.close()
    return task


def update_task(task: TaskDB):
    db = get_db()
    db.merge(task)
    db.commit()
    db.close()


def delete_task(task_id: str) -> bool:
    db = get_db()
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        db.close()
        return False

    db.delete(task)
    db.commit()
    db.close()
    return True
