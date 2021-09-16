# test hello_flask.py
from hello_flask import app

def test_hello_flask():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'