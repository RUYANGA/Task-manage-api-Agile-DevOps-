"""Tests for the task update endpoint."""

from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function() -> None:
    """Reset the in-memory task store before each test."""
    reset()


def test_update_task_title() -> None:
    """Verify that a task's title can be updated."""
    client.post("/tasks", json={"title": "Old task"})
    res = client.put("/tasks/1", json={"title": "New task"})
    assert res.status_code == 200
    assert res.json()["title"] == "New task"


def test_update_task_completed() -> None:
    """Verify that a task's completion status can be updated."""
    client.post("/tasks", json={"title": "Task"})
    res = client.put("/tasks/1", json={"title": "Task", "completed": True})
    assert res.status_code == 200
    assert res.json()["completed"] is True


def test_update_task_not_found() -> None:
    """Verify that updating a non-existent task returns a 404 error."""
    res = client.put("/tasks/999", json={"title": "Ghost"})
    assert res.status_code == 404
    assert res.json()["detail"] == "Task not found"
