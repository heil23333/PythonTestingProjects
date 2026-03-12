import requests
from config import BASE_URL, TIMEOUT

def test_product_list():
    resp = requests.get(
        f"{BASE_URL}/api/v1/products",
        params={
            "page": 1,
            "page_size": 3,
        },
        timeout=TIMEOUT
    )
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["message"] == "success"
    assert body["data"]["page"] == 1
    assert body["data"]["page_size"] == 3
    assert len(body["data"]["items"]) <= 3
