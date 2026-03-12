import requests

def test_demo():
    assert 1 + 1 == 2

def test_health():
    resp = requests.get("http://127.0.0.1:5001/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["data"]["status"] == "ok"
