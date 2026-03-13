def assert_success_response(resp, body, code = 0, message = "success", status_code=200):
    assert resp.status_code == status_code
    assert body["code"] == code
    assert body["message"] == message