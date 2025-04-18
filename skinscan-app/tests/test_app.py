import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to SkinScan.AI" in response.data

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About SkinScan.AI" in response.data