from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.services import task_service
from app.services.csv_collector import import_csv
from app.services.task_service import update_task

scheduler = BackgroundScheduler()


def start_scheduler():
    print(">>> SCHEDULER STARTED <<<")
    scheduler.start()


def run_task(task_id: str):
    print(f">>> run_task EXECUTED for {task_id}")

    task = task_service.get_task(task_id)
    if not task:
        return

    task.status = "running"
    task.last_run = datetime.utcnow()
    update_task(task)

    try:
        if task.task_type == "csv_import":
            rows = import_csv(task.filename)
            print(
                f">>> CSV IMPORT DONE | file={task.filename} | rows={rows}"
            )

        task.status = "done"
        update_task(task)

    except Exception as e:
        task.status = "failed"
        print(f">>> TASK ERROR: {e}")



def schedule_task(task_id: str):
    task = task_service.get_task(task_id)
    if not task:
        return

    print(f">>> ADDING JOB {task_id} every {task.interval_seconds}s")

    scheduler.add_job(
        run_task,
        trigger="interval",
        seconds=task.interval_seconds,
        args=[task_id],
        id=task_id,
        replace_existing=True,
    )
