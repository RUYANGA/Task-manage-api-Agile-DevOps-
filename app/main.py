from fastapi import FastAPI, HTTPException

from app.models import Task, TaskCreate
from app.tasks import tasks
from app.logger import logger

app = FastAPI(
    title="Task Management API",
    description="A REST API for managing tasks, built with FastAPI.",
    version="1.0.0",
)


@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Task API"}


@app.get("/health")
def health():
    logger.info("Health check passed")
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        completed=False,
    )
    tasks.append(new_task)
    logger.info(f"Task created: id={new_task.id}, title={new_task.title}")
    return new_task


@app.get("/tasks")
def get_tasks():
    logger.info(f"Tasks listed: {len(tasks)} items")
    return tasks


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskCreate):
    for task in tasks:
        if task.id == task_id:
            task.title = updated.title
            logger.info(f"Task updated: id={task_id}, new_title={updated.title}")
            return task
    logger.error(f"Task not found: id={task_id}")
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            logger.info(f"Task deleted: id={task_id}")
            return {"message": "Task deleted"}
    logger.error(f"Task not found: id={task_id}")
    raise HTTPException(status_code=404, detail="Task not found")
