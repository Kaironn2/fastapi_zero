from http import HTTPStatus


def test_root_returns_hello_world(client):
    response = client.get('/')

    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK


def test_get_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'user': 'bob',
            'email': 'bob@gmail.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'user': 'bob',
        'email': 'bob@gmail.com',
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'user': 'bob',
            'email': 'bob@gmail.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'user': 'bob',
        'email': 'bob@gmail.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/4',
        json={
            'user': 'bob',
            'email': 'bob@gmail.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'user': 'bob',
        'email': 'bob@gmail.com',
    }


def test_delete_user_not_found(client):
    response = client.delete('/users/4')

    assert response.status_code == HTTPStatus.NOT_FOUND
