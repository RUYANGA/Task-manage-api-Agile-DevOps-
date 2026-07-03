"""In-memory task storage and lifecycle utilities."""

from app.models import Task

tasks: list[Task] = []
"""In-memory store for all active tasks."""


def reset() -> None:
    """Clear all tasks from the in-memory store.

    This is primarily used during testing to ensure a clean state
    between test cases.
    """
    tasks.clear()
