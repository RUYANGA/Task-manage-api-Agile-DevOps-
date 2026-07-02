from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function():
    reset()


def test_update_task():

    client.post("/tasks", json={"title": "Old task"})

    res = client.put("/tasks/1", json={"title": "New task"})

    assert res.status_code == 200
    assert res.json()["title"] == "New task"