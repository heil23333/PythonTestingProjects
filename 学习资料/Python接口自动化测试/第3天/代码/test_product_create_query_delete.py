import requests
from config import BASE_URL, TIMEOUT
from pathlib import Path
import json

DATA_FILE = Path(__file__).parent/"data"/"new_product_case.json"
NEW_PRODUCT_CASE = json.loads(DATA_FILE.read_text(encoding="utf-8"))

def test_product_create_query_delete(auth_headers):
    create_resp = requests.post(
        f"{BASE_URL}/api/v1/products",
        headers=auth_headers,
        json={
            "name": NEW_PRODUCT_CASE["name"],
            "category": NEW_PRODUCT_CASE["category"],
            "price": NEW_PRODUCT_CASE["price"]
        },
        timeout=TIMEOUT
    )
    create_body = create_resp.json()

    assert create_resp.status_code == 201
    assert create_body["code"] == 0
    assert create_body["message"] == "success"

    product_id = create_body["data"]["id"]

    detail_resp = requests.get(
        f"{BASE_URL}/api/v1/products/{product_id}",
        timeout=TIMEOUT
    )
    detail_body = detail_resp.json()

    assert detail_resp.status_code == 200
    assert detail_body["code"] == 0
    assert detail_body["data"]["id"] == product_id
    assert detail_body["data"]["name"] == "Desk Lamp"
    assert detail_body["data"]["price"] == 199
    assert detail_body["data"]["category"] == "lighting"

    delete_resp = requests.delete(
        f"{BASE_URL}/api/v1/products/{product_id}",
        headers=auth_headers,
        timeout=TIMEOUT
    )
    delete_body = delete_resp.json()

    assert delete_resp.status_code == 200
    assert delete_body["code"] == 0
    assert delete_body["message"] == "success"
    assert delete_body["data"]["deleted"] is True

    query_resp = requests.get(f"{BASE_URL}/api/v1/products/{product_id}", timeout=TIMEOUT)
    query_body = query_resp.json()

    assert query_resp.status_code == 404
    assert query_body["code"] == 10041
    assert query_body["message"] == "product not found"
