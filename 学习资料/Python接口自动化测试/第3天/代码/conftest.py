import pytest
import requests
from config import BASE_URL, PASSWORD, USERNAME, TIMEOUT

@pytest.fixture
def reset_data():
    requests.post(f"{BASE_URL}/api/v1/debug/reset", timeout=TIMEOUT)


@pytest.fixture
def login_token(reset_data):
    resp = requests.post(
        f"{BASE_URL}/api/v1/login",
        json={
            "username": USERNAME,
            "password": PASSWORD
        }
    )
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0

    return body["data"]["token"]

@pytest.fixture
def auth_headers(login_token):
    return {"Authorization": f"Bearer {login_token}"}