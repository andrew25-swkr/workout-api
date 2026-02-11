from fastapi import FastAPI
from app.core.database import engine, Base
from app.api import workout

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workout API")

app.include_router(workout.router)