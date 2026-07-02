from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function():
    reset()


def test_create_task():
    res = client.post("/tasks", json={"title": "Buy groceries"})
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "Buy groceries"
    assert data["completed"] is False
    assert data["id"] == 1


def test_create_task_empty_title():
    res = client.post("/tasks", json={"title": ""})
    assert res.status_code == 200


def test_create_task_missing_title():
    res = client.post("/tasks", json={})
    assert res.status_code == 422


def test_create_task_with_completed_true():
    res = client.post("/tasks", json={"title": "Done task", "completed": True})
    assert res.status_code == 200
    data = res.json()
    assert data["completed"] is True


def test_create_task_with_completed_false():
    res = client.post("/tasks", json={"title": "Pending task", "completed": False})
    assert res.status_code == 200
    data = res.json()
    assert data["completed"] is False
