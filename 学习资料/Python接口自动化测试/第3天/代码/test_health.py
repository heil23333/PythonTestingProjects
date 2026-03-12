import requests
from config import BASE_URL


def test_health():
    resp = requests.get(f"{BASE_URL}/health")

    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["message"] == "success"
    assert body["data"]["status"] == "ok"