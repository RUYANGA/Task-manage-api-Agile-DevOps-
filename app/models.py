"""Pydantic models for the Task Management API."""

from pydantic import BaseModel


class Task(BaseModel):
    """Represents a task entity with its core attributes.

    Attributes:
        id: The unique identifier for the task.
        title: The title or name of the task.
        completed: Flag indicating whether the task has been completed.
            Defaults to False.
    """

    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    """Schema for creating a new task.

    Attributes:
        title: The title of the task to create.
        completed: Optional initial completion status. When omitted, the
            task defaults to incomplete.
    """

    title: str
    completed: bool | None = None
