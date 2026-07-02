from fastapi.testclient import TestClient
from app.main import app
from app.tasks import reset

client = TestClient(app)


def setup_function():
    reset()


def test_delete_task():

    client.post("/tasks", json={"title": "Task to delete"})

    res = client.delete("/tasks/1")

    assert res.status_code == 200
    assert res.json()["message"] == "Task deleted"