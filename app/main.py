"""FastAPI application entry point with REST endpoints for task management."""

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
def home() -> dict[str, str]:
    """Return a welcome message for the API root endpoint.

    Returns:
        A dictionary containing a greeting message.
    """
    logger.info("Home endpoint accessed")
    return {"message": "Task API"}


@app.get("/health")
def health() -> dict[str, str]:
    """Perform a health check on the API.

    Returns:
        A dictionary indicating the service health status.
    """
    logger.info("Health check passed")
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: TaskCreate) -> Task:
    """Create a new task.

    Args:
        task: The task creation payload containing title and optional
            completion status.

    Returns:
        The newly created Task with an auto-generated identifier.
    """
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        completed=task.completed if task.completed is not None else False,
    )
    tasks.append(new_task)
    logger.info(f"Task created: id={new_task.id}, title={new_task.title}")
    return new_task


@app.get("/tasks")
def get_tasks() -> list[Task]:
    """Retrieve all tasks from the in-memory store.

    Returns:
        A list of all current Task objects.
    """
    logger.info(f"Tasks listed: {len(tasks)} items")
    return tasks


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskCreate) -> Task:
    """Update an existing task's title and/or completion status.

    Args:
        task_id: The unique identifier of the task to update.
        updated: The updated task data.

    Returns:
        The updated Task object.

    Raises:
        HTTPException: If no task with the given ID exists (404).
    """
    for task in tasks:
        if task.id == task_id:
            task.title = updated.title
            if updated.completed is not None:
                task.completed = updated.completed
            logger.info(
                f"Task updated: id={task_id}, "
                f"title={task.title}, completed={task.completed}"
            )
            return task
    logger.error(f"Task not found: id={task_id}")
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    """Delete a task by its unique identifier.

    Args:
        task_id: The unique identifier of the task to delete.

    Returns:
        A confirmation message indicating successful deletion.

    Raises:
        HTTPException: If no task with the given ID exists (404).
    """
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            logger.info(f"Task deleted: id={task_id}")
            return {"message": "Task deleted"}
    logger.error(f"Task not found: id={task_id}")
    raise HTTPException(status_code=404, detail="Task not found")
