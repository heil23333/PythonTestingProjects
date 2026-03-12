import requests
from config import BASE_URL

def test_demo():
    assert 1 + 1 == 2

def test_health():
    resp = requests.get(f"{BASE_URL}/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["data"]["status"] == "ok"
