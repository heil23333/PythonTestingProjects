import pytest
from common.request_handler import send_request
from common.assert_util import assert_success_response
import json
from pathlib import Path

from config.settings import BASE_URL

DATA_FILE = Path(__file__).parent.parent/"data"/"login_cases.json"
LOGIN_CASES = json.loads(DATA_FILE.read_text(encoding="utf-8"))

@pytest.mark.parametrize("case", LOGIN_CASES)
def test_login(case):
    resp = send_request(
        "POST", 
        f"{BASE_URL}/api/v1/login",
        json={"username": case["username"], "password": case["password"]}
    )
    
    body = resp.json()

    assert_success_response(resp, body, code=case["expected_code"], message=case["expected_message"], status_code=case["expected_status"])

    if case["expected_code"] == 0:
        assert "token" in body["data"]
        assert body["data"]["user"]["username"] == case["username"]
    else:
        assert body["data"] is None
    
