import requests
import pytest

from config import BASE_URL, TIMEOUT

@pytest.mark.parametrize(
    "product_id, status_code, code, message",
    [
        (1, 200, 0, "success"),
        (10, 404, 10041, "product not found"),
    ]
)
def test_products(product_id, status_code, code, message):
    resp = requests.get(
        f"{BASE_URL}/api/v1/products/{product_id}",
        timeout=TIMEOUT
    )
    
    assert resp.status_code == status_code
    body = resp.json()
    assert body["code"] == code
    assert body["message"] == message