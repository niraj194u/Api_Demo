# test_simple_api.py

import pytest
from simple_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greet(client):
    response = client.post('/greet', json={"name": "Alice"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alice!"}

def test_greet_no_name(client):
    response = client.post('/greet', json={})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Guest!"}
