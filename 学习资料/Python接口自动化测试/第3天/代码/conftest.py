import pytest
from common.request_handler import send_request
from config.settings import BASE_URL, PASSWORD, USERNAME
from common.assert_util import assert_success_response

@pytest.fixture
def reset_data():
    reset_resp = send_request("POST", f"{BASE_URL}/api/v1/debug/reset")
    assert reset_resp.json()["data"]["reset"] == True
    assert_success_response(reset_resp, reset_resp.json(), message="data reset")


@pytest.fixture
def login_token(reset_data):
    resp = send_request(
        "POST", 
        f"{BASE_URL}/api/v1/login",
        json={
            "username": USERNAME,
            "password": PASSWORD
        }
    )
    
    body = resp.json()

    assert_success_response(resp, body)

    return body["data"]["token"]

@pytest.fixture
def auth_headers(login_token):
    return {"Authorization": f"Bearer {login_token}"}