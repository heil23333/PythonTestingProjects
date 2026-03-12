import requests

BASE_URL = "http://127.0.0.1:5001"

def test_profile(login_token):
    headers = {"Authorization": f"Bearer {login_token}"}
    resp = requests.get(f"{BASE_URL}/api/v1/profile", headers=headers)
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["message"] == "success"
    assert body["data"]["username"] == "alice"