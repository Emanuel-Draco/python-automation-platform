from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.services import task_service
from app.services.csv_collector import import_csv

scheduler = BackgroundScheduler()


def start_scheduler():
    print(">>> SCHEDULER STARTED <<<")
    scheduler.start()


def run_task(task_id: str):
    print(f">>> run_task EXECUTED for {task_id}")

    task = task_service.get_task(task_id)
    if not task:
        print(">>> TASK NOT FOUND")
        return

    task.status = "running"
    task.last_run = datetime.utcnow()

    if task.task_type == "csv_import":
        rows = import_csv("sample.csv")
        print(f">>> CSV IMPORT DONE, rows={rows}")

    task.status = "done"


def schedule_task(task_id: str):
    print(f">>> ADDING JOB {task_id}")

    scheduler.add_job(
        run_task,
        trigger="interval",
        seconds=5,
        args=[task_id],
        id=task_id,
        replace_existing=True
    )
