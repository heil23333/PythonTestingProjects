import requests

base_url = "http://127.0.0.1:5001"

# get_req = requests.get(f"{base_url}/health")

# print(get_req.status_code)
# print(get_req.json())

# print("\n")

products_req = requests.get(
    f"{base_url}/api/v1/products", 
    params={
        "page": 1, 
        "page_size": 5, 
        # "page_size": -1, 
        "keyword": "keyboard"
        }
    )

print(products_req.url)
print(products_req.status_code)
print(products_req.json())

# print("\n")

# login_req = requests.post(
#     f"{base_url}/api/v1/login", 
#     json={"username": "alice", "password": "123456"}
# )

# token = login_req.json()["data"]["token"]

# profile_req = requests.get("http://127.0.0.1:5001/api/v1/profile", headers={"Authorization": f"Bearer {token}"})
# print(profile_req.status_code)
# print(profile_req.json())

# add_product_req = requests.post("http://127.0.0.1:5001/api/v1/products", 
#                                 json={"name": "heli", "category": "person", "price": 9999},
#                                 headers={"Authorization": f"Bearer {token}"})
# print(add_product_req.status_code)
# print(add_product_req.json())

# get_product_req = requests.get("http://127.0.0.1:5001/api/v1/products/6")
# print(get_product_req.json())

# delete_product_req = requests.delete("http://127.0.0.1:5001/api/v1/products/6"
#                                      , headers={"Authorization": f"Bearer {token}"})
# print(delete_product_req.status_code)
# print(delete_product_req.json())

# get_product_req = requests.get("http://127.0.0.1:5001/api/v1/products/6")
# print(get_product_req.text)