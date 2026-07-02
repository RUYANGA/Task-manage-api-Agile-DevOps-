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



@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskCreate):

    for task in tasks:
        if task.id == task_id:
            task.title = updated.title

            logger.info(f"Task {task_id} updated")

            return task

    logger.error(f"Task {task_id} not found")
    raise HTTPException(status_code=404, detail="Task not found")



@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)

            logger.info(f"Task {task_id} deleted")

            return {"message": "Task deleted"}

    logger.error(f"Task {task_id} not found")
    raise HTTPException(status_code=404, detail="Task not found")