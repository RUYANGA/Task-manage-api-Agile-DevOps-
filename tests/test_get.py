"""Tests for the task retrieval endpoint."""

from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function() -> None:
    """Reset the in-memory task store before each test."""
    reset()


def test_get_tasks_empty() -> None:
    """Verify that an empty task list returns an empty array."""
    res = client.get("/tasks")
    assert res.status_code == 200
    assert res.json() == []


def test_get_tasks_with_data() -> None:
    """Verify that the endpoint returns all created tasks."""
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    res = client.get("/tasks")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"
