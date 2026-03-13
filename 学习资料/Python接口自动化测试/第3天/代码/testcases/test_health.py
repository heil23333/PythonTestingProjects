from common.request_handler import send_request
from common.assert_util import assert_success_response
from config.settings import BASE_URL

def test_health():
    resp = send_request("GET", f"{BASE_URL}/health")

    body = resp.json()

    assert_success_response(resp, body)
    assert body["data"]["status"] == "ok"