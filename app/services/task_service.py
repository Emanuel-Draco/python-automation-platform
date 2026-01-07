from app.models.task import Task

_tasks: dict[str, Task] = {}


def create_task(name: str, task_type: str, schedule: str) -> Task:
    task = Task(name=name, task_type=task_type, schedule=schedule)
    _tasks[task.id] = task
    return task


def list_tasks() -> list[Task]:
    return list(_tasks.values())


def get_task(task_id: str) -> Task | None:
    return _tasks.get(task_id)


def delete_task(task_id: str) -> bool:
    return _tasks.pop(task_id, None) is not None
