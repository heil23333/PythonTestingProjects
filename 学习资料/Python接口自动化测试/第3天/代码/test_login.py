import pytest
import requests

BASE_URL = "http://127.0.0.1:5001"


@pytest.mark.parametrize(
    "username,password,expected_status,expected_code",
    [
        ("alice", "123456", 200, 0),
        ("alice", "wrong", 401, 10014),
        ("", "123456", 400, 10011),
        ("heli", "123456", 404, 10013),
        ("", "", 400, 10011)
    ],
)
def test_login(username, password, expected_status, expected_code):
    resp = requests.post(
        f"{BASE_URL}/api/v1/login",
        json={"username": username, "password": password},
    )
    body = resp.json()

    assert resp.status_code == expected_status
    assert body["code"] == expected_code

    if expected_code == 0:
        assert body["message"] == "success"
        assert "token" in body["data"]
        assert body["data"]["user"]["username"] == username
    else:
        assert body["data"] is None
