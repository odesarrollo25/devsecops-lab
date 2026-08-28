from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "name": "DevSecOps Task API",
        "version": "0.2.0",
        "status": "running",
    }
