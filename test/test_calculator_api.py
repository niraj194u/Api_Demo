# test_calculator_api.py

import pytest
from calculator_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.post('/add', json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5

def test_subtract(client):
    response = client.post('/subtract', json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.get_json()['result'] == 1

def test_multiply(client):
    response = client.post('/multiply', json={"a": 3, "b": 2})
    assert response.status_code == 200
    assert response.get_json()['result'] == 6

def test_divide(client):
    response = client.post('/divide', json={"a": 6, "b": 2})
    assert response.status_code == 200
    assert response.get_json()['result'] == 3

def test_divide_by_zero(client):
    response = client.post('/divide', json={"a": 6, "b": 0})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Cannot divide by zero"
