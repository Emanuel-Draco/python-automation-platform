from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.services import task_service

scheduler = BackgroundScheduler()


def run_task(task_id: str):
    task = task_service.get_task(task_id)
    if not task:
        return

    task.status = "running"
    task.last_run = datetime.utcnow()

    # 🔧 TU symulujemy prawdziwą pracę
    print(f"[SCHEDULER] Running task: {task.name}")

    # Po wykonaniu
    task.status = "done"


def schedule_task(task_id: str, seconds: int = 10):
    scheduler.add_job(
        run_task,
        "interval",
        seconds=seconds,
        args=[task_id],
        id=task_id,
        replace_existing=True
    )
