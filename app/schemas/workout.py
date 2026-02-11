from pydantic import BaseModel

class WorkoutCreate(BaseModel):
    name: str
    duration: int

class WorkoutResponse(WorkoutCreate):
    id: int

    class Config:
        from_attributes = True