from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function():
    reset()


def test_get_tasks_empty():
    res = client.get("/tasks")
    assert res.status_code == 200
    assert res.json() == []


def test_get_tasks_with_data():
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    res = client.get("/tasks")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"
