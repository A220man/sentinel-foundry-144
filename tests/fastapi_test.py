from fastapi.testclient import TestClient
from src.fastapi_app import app

client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Hello, world!"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "ok"}


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data == {"version": "1.1.0"}
