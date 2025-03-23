# main.py – Task Manager API using FastAPI

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Pydantic model representing a Task
class Task(BaseModel):
    id: int                # unique identifier for the task
    title: str             # short title of the task
    description: str | None = None  # optional detailed description
    completed: bool = False         # status flag

# In-memory "database" of tasks (stored in a dict for simplicity)
tasks_db: dict[int, Task] = {}

# CREATE – Endpoint to add a new task
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """
    Create a new task. The task data is sent in the request body as JSON.
    The new task is added to the tasks_db and returned.
    """
    tasks_db[task.id] = task
    return task

# READ (all) – Endpoint to get the list of all tasks
@app.get("/tasks", response_model=list[Task])
def list_tasks():
    """
    Retrieve all tasks. Returns a list of Task objects.
    """
    return list(tasks_db.values())

# READ (one) – Endpoint to get a single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    """
    Get a specific task by its ID. Returns the Task if found.
    """
    return tasks_db.get(task_id)

# UPDATE – Endpoint to update an existing task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated: Task):
    """
    Update an existing task. The full Task is provided in the request body.
    If the task exists, update it; otherwise, this creates a new task.
    """
    tasks_db[task_id] = updated
    return updated

# DELETE – Endpoint to delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Delete a task from the database. Returns a message upon success.
    """
    tasks_db.pop(task_id, None)
    return {"message": "Task deleted successfully"}
