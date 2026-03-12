import pytest
import requests

BASE_URL = "http://127.0.0.1:5001"

@pytest.fixture
def login_token():
    resp = requests.post(
        f"{BASE_URL}/api/v1/login",
        json={
            "username": "alice",
            "password": "123456"
        }
    )
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0

    return body["data"]["token"]

@pytest.fixture
def base_url():
    return "http://127.0.0.1:5001"