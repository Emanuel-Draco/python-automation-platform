from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.routes import router
from app.services.scheduler import start_scheduler

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def startup_event():
    init_db()
    start_scheduler()
