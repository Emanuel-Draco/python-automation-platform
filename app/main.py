from fastapi import FastAPI
from app.api.routes import router
from app.services.scheduler import start_scheduler

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def startup_event():
    start_scheduler()
