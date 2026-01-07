from fastapi import FastAPI
from app.api.routes import router
from app.services.scheduler import scheduler

app = FastAPI(
    title="Python Automation Platform",
    version="0.2.0"
)

app.include_router(router)


@app.on_event("startup")
def start_scheduler():
    scheduler.start()


@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown()
