from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    name: str
    task_type: str
    schedule: str


class TaskResponse(BaseModel):
    id: str
    name: str
    task_type: str
    schedule: str
    status: str
    last_run: Optional[datetime]
    created_at: datetime
