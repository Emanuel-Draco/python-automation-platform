from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    name: str
    task_type: str
    schedule: str

    filename: Optional[str] = Field(
        default=None,
        description="CSV filename for csv_import tasks"
    )

    interval_seconds: int = Field(
        default=10,
        ge=1,
        le=3600,
        description="Execution interval in seconds"
    )


class TaskResponse(BaseModel):
    id: str
    name: str
    task_type: str
    schedule: str

    filename: Optional[str]
    interval_seconds: int

    status: str
    last_run: Optional[datetime]
    created_at: datetime

