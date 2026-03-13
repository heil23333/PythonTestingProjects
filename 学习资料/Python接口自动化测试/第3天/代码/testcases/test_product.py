from common.request_handler import send_request
import pytest
from common.assert_util import assert_success_response
from config.settings import BASE_URL

@pytest.mark.parametrize(
    "product_id, status_code, code, message",
    [
        (1, 200, 0, "success"),
        (10, 404, 10041, "product not found"),
    ]
)
def test_products(product_id, status_code, code, message):
    resp = send_request("GET", f"{BASE_URL}/api/v1/products/{product_id}")

    body = resp.json()
    
    assert_success_response(resp, body, code, message, status_code)