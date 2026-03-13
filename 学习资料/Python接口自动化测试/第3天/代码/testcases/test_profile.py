from common.request_handler import send_request
from config.settings import BASE_URL
from common.assert_util import assert_success_response

def test_profile(login_token):
    headers = {"Authorization": f"Bearer {login_token}"}
    resp = send_request("GET", f"{BASE_URL}/api/v1/profile", headers=headers)
    body = resp.json()

    assert_success_response(resp, body)
    assert body["data"]["username"] == "alice"