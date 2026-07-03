"""Tests for the task deletion endpoint."""

from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function() -> None:
    """Reset the in-memory task store before each test."""
    reset()


def test_delete_task() -> None:
    """Verify that an existing task can be deleted successfully."""
    client.post("/tasks", json={"title": "Task to delete"})
    res = client.delete("/tasks/1")
    assert res.status_code == 200
    assert res.json()["message"] == "Task deleted"
