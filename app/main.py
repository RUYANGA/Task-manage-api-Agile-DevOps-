from fastapi import FastAPI, HTTPException

from app.models import Task, TaskCreate
from app.tasks import tasks
from app.logger import logger

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/tasks")
def create_task(task: TaskCreate):

    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        completed=False
    )

    tasks.append(new_task)

    logger.info("Task created")

    return new_task

@app.get("/tasks")
def get_tasks():
    return tasks