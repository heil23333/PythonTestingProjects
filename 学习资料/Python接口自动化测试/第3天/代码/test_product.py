import requests
import pytest

@pytest.mark.parametrize(
    "product_id, status_code, code, message",
    [
        (1, 200, 0, "success"),
        (10, 404, 10041, "product not found"),
    ]
)
def test_products(base_url, product_id, status_code, code, message):
    resp = requests.get(
        f"{base_url}/api/v1/products/{product_id}"
    )
    
    assert resp.status_code == status_code
    body = resp.json()
    assert body["code"] == code
    assert body["message"] == message