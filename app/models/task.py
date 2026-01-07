from datetime import datetime
from uuid import uuid4


class Task:
    def __init__(self, name: str, task_type: str, schedule: str):
        self.id = str(uuid4())
        self.name = name
        self.task_type = task_type
        self.schedule = schedule
        self.status = "pending"
        self.last_run = None
        self.created_at = datetime.utcnow()
