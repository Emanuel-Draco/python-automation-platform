from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from app.db.session import Base
from uuid import uuid4


class Task:
    def __init__(
        self,
        name: str,
        task_type: str,
        schedule: str,
        filename: str | None = None,
        interval_seconds: int = 10,
    ):
        self.id = str(uuid4())
        self.name = name
        self.task_type = task_type
        self.schedule = schedule

        self.filename = filename
        self.interval_seconds = interval_seconds

        self.status = "pending"
        self.last_run = None
        self.created_at = datetime.utcnow()


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    task_type = Column(String, nullable=False)
    schedule = Column(String, nullable=False)

    filename = Column(String, nullable=True)
    interval_seconds = Column(Integer, default=10)

    status = Column(String, default="pending")
    last_run = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)