from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app import crud
from app.schemas import workout as schema

router = APIRouter(prefix="/workouts", tags=["Workout"])

#DB 세션 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.WorkoutResponse)
def create(workout: schema.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.workout.create_workout(db, workout)

@router.get("/", response_model=list[schema.WorkoutResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.workout.get_workouts(db)