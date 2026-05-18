from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_request_id_header_exists():
    response = client.get("/health")

    assert response.status_code == 200
    assert "X-Request-ID" in response.headers