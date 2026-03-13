from common.request_handler import send_request
from config.settings import BASE_URL
from common.assert_util import assert_success_response

def test_product_list():
    resp = send_request(
        "GET", 
        f"{BASE_URL}/api/v1/products", 
        params={
            "page": 1,
            "page_size": 3,
        }
    )
    
    body = resp.json()

    assert_success_response(resp, body)
    assert body["data"]["page"] == 1
    assert body["data"]["page_size"] == 3
    assert len(body["data"]["items"]) <= 3
