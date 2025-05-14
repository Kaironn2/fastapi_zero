from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app


def test_hello_world_html():
    client = TestClient(app)
    response = client.get('/hello-world')

    assert '<h1>Olá, mundo!</h1>' in response.text
    assert response.status_code == HTTPStatus.OK
