"""Tests for the health-check endpoint."""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health() -> None:
    """Verify that the /health endpoint returns a healthy status."""
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"
