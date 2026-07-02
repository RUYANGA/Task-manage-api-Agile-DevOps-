from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_task():

    client.post("/tasks", json={"title": "Old task"})

    res = client.put("/tasks/1", json={"title": "New task"})

    assert res.status_code == 200
    assert res.json()["title"] == "New task"