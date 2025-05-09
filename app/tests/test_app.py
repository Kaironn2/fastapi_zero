from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app


def test_root_returns_hello_world():
    client = TestClient(app)
    response = client.get('/')

    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK
