import pytest
import requests
import json
from pathlib import Path

from config import BASE_URL

DATA_FILE = Path(__file__).parent/"data"/"login_cases.json"
LOGIN_CASES = json.loads(DATA_FILE.read_text(encoding="utf-8"))

@pytest.mark.parametrize("case", LOGIN_CASES)
def test_login(case):
    resp = requests.post(
        f"{BASE_URL}/api/v1/login",
        json={"username": case["username"], "password": case["password"]},
    )
    body = resp.json()

    assert resp.status_code == case["expected_status"]
    assert body["code"] == case["expected_code"]

    if case["expected_code"] == 0:
        assert body["message"] == case["expected_message"]
        assert "token" in body["data"]
        assert body["data"]["user"]["username"] == case["username"]
    else:
        assert body["data"] is None
