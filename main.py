from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

app = FastAPI()

# Step 1: Define allowed status values using Enum
class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

# Step 2: Define the structure of a Task using Pydantic
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.pending

# Step 3: Simulate database with an in-memory list
tasks: List[Task] = []
task_counter = 1

# Step 4: Define your routes
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    global task_counter
    task.id = task_counter
    task_counter += 1
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return
    raise HTTPException(status_code=404, detail="Task not found")



@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task.id = task_id  # Preserve the original ID
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")