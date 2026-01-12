from app.db.session import Base, engine
from app.models.task import TaskDB


def init_db():
    Base.metadata.create_all(bind=engine)
