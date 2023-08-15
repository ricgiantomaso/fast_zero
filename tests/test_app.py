from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_olamundo_e_200():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Olá mundo'}


""" def test_update_user_not_found(client, user):
    response = client.put(
        '/users/0',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}

def test_delete_user_not_found(client, user):
    response = client.delete('/users/0')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}

"""
