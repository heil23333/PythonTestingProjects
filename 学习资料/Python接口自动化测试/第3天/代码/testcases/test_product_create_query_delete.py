from common.request_handler import send_request
from common.assert_util import assert_success_response
from config.settings import BASE_URL
from pathlib import Path
import json

DATA_FILE = Path(__file__).resolve().parent.parent/"data"/"new_product_case.json"
NEW_PRODUCT_CASE = json.loads(DATA_FILE.read_text(encoding="utf-8"))[0]

def test_product_create_query_delete(auth_headers):
    create_resp = send_request(
        "POST",
        f"{BASE_URL}/api/v1/products",
        headers=auth_headers,
        json={
            "name": NEW_PRODUCT_CASE["name"],
            "category": NEW_PRODUCT_CASE["category"],
            "price": NEW_PRODUCT_CASE["price"]
        }
    )
    create_body = create_resp.json()

    assert_success_response(create_resp, create_body, status_code=201)

    product_id = create_body["data"]["id"]

    detail_resp = send_request("GET", f"{BASE_URL}/api/v1/products/{product_id}")
    detail_body = detail_resp.json()

    assert_success_response(detail_resp, detail_body)
    assert detail_body["data"]["id"] == product_id
    assert detail_body["data"]["name"] == NEW_PRODUCT_CASE["name"]
    assert detail_body["data"]["price"] == NEW_PRODUCT_CASE["price"]
    assert detail_body["data"]["category"] == NEW_PRODUCT_CASE["category"]

    delete_resp = send_request("DELETE", f"{BASE_URL}/api/v1/products/{product_id}", headers=auth_headers)
    delete_body = delete_resp.json()

    assert_success_response(delete_resp, delete_body)
    assert delete_body["data"]["deleted"] is True

    query_resp = send_request("GET", f"{BASE_URL}/api/v1/products/{product_id}")
    query_body = query_resp.json()

    assert query_resp.status_code == 404
    assert query_body["code"] == 10041
    assert query_body["message"] == "product not found"
