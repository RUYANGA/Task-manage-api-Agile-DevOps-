from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function():
    reset()


def test_update_task_title():

    client.post("/tasks", json={"title": "Old task"})

    res = client.put("/tasks/1", json={"title": "New task"})

    assert res.status_code == 200
    assert res.json()["title"] == "New task"


def test_update_task_completed():

    client.post("/tasks", json={"title": "Task"})

    res = client.put("/tasks/1", json={"title": "Task", "completed": True})

    assert res.status_code == 200
    assert res.json()["completed"] is True


def test_update_task_not_found():
    res = client.put("/tasks/999", json={"title": "Ghost"})
    assert res.status_code == 404
    assert res.json()["detail"] == "Task not found"