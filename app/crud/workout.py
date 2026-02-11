from sqlalchemy.orm import Session
from app.models.workout import Workout
from app.schemas.workout import WorkoutCreate

def create_workout(db: Session, workout: WorkoutCreate):
    db_workout = Workout(name=workout.name, duration=workout.duration)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts(db: Session):
    return db.query(Workout).all()