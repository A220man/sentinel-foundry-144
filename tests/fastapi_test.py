from fastapi.testclient import TestClient
from src.fastapi_app import app

client = TestClient(app)

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Hello, world!"}
