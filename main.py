from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

app = FastAPI()

class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.pending