"""Tests for the task creation endpoint."""

from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function() -> None:
    """Reset the in-memory task store before each test."""
    reset()


def test_create_task() -> None:
    """Verify that a basic task can be created successfully."""
    res = client.post("/tasks", json={"title": "Buy groceries"})
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "Buy groceries"
    assert data["completed"] is False
    assert data["id"] == 1


def test_create_task_empty_title() -> None:
    """Verify that a task with an empty title string is accepted."""
    res = client.post("/tasks", json={"title": ""})
    assert res.status_code == 200


def test_create_task_missing_title() -> None:
    """Verify that omitting the title field returns a validation error."""
    res = client.post("/tasks", json={})
    assert res.status_code == 422


def test_create_task_with_completed_true() -> None:
    """Verify that a task can be created with the completed flag set to True."""
    res = client.post("/tasks", json={"title": "Done task", "completed": True})
    assert res.status_code == 200
    data = res.json()
    assert data["completed"] is True


def test_create_task_with_completed_false() -> None:
    """Verify that a task can be created with the completed flag set to False."""
    res = client.post("/tasks", json={"title": "Pending task", "completed": False})
    assert res.status_code == 200
    data = res.json()
    assert data["completed"] is False
