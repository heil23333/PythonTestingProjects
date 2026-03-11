import requests

print("**********分割线***********\n")
resp1 = requests.get("http://127.0.0.1:5001/health")
print(resp1.url)
print(resp1.status_code)
print(resp1.json())

print("\n**********分割线***********\n")
resp2 = requests.get("http://127.0.0.1:5001/api/v1/products", params={"page": 1, "page_size": 3, "keyword": "mouse"})
print(resp2.url)
print(resp2.json())

print("\n**********分割线***********\n")
resp3 = requests.post("http://127.0.0.1:5001/api/v1/login", json={"username": "alice", "password": "123456"})

print(resp3.url)
print(resp3.status_code)
print(resp3.json())

print("\n**********分割线***********\n")

resp4 = requests.post(
    "http://127.0.0.1:5001/api/v1/echo-form",
    data={"name": "alice", "city": "shanghai"}
)
print(resp4.json())

print("\n**********分割线***********\n")

login_resp = requests.post("http://127.0.0.1:5001/api/v1/login", json={"username": "alice", "password": "123456"})
token = login_resp.json()["data"]["token"]

print(token)

profile_resp = requests.get(
    "http://127.0.0.1:5001/api/v1/profile",
    headers={"Authorization": f"Bearer {token}"},
)
print(profile_resp.json())

print("\n**********分割线***********\n")