from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from flask import Flask, jsonify, request


BASE_DIR = Path(__file__).resolve().parent.parent
SEED_FILE = BASE_DIR / "data" / "seed.json"

app = Flask(__name__)


def load_seed() -> dict:
    return json.loads(SEED_FILE.read_text(encoding="utf-8"))


STATE = load_seed()
TOKENS: dict[str, dict] = {}


def success(data=None, message: str = "success", status: int = 200):
    return jsonify({"code": 0, "message": message, "data": data}), status


def failure(code: int, message: str, status: int):
    return jsonify({"code": code, "message": message, "data": None}), status


def current_user():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth.split(" ", 1)[1].strip()
    return TOKENS.get(token)


def find_user(username: str):
    for user in STATE["users"]:
        if user["username"] == username:
            return user
    return None


def next_product_id() -> int:
    if not STATE["products"]:
        return 1
    return max(item["id"] for item in STATE["products"]) + 1


@app.get("/health")
def health():
    return success({"status": "ok"})


@app.post("/api/v1/debug/reset")
def reset_data():
    global STATE
    STATE = deepcopy(load_seed())
    TOKENS.clear()
    return success({"reset": True}, message="data reset")


@app.post("/api/v1/login")
def login():
    payload = request.get_json(silent=True)
    if not payload:
        return failure(10010, "json body required", 400)

    username = payload.get("username", "").strip()
    password = payload.get("password", "").strip()

    if not username:
        return failure(10011, "username required", 400)
    if not password:
        return failure(10012, "password required", 400)

    user = find_user(username)
    if not user:
        return failure(10013, "user not found", 404)
    if user["password"] != password:
        return failure(10014, "password error", 401)

    token = f"token-{user['id']}"
    TOKENS[token] = user
    return success(
        {
            "token": token,
            "user": {
                "id": user["id"],
                "username": user["username"],
                "role": user["role"],
                "nickname": user["nickname"],
            },
        }
    )


@app.get("/api/v1/profile")
def profile():
    user = current_user()
    if not user:
        return failure(10021, "token required", 401)

    return success(
        {
            "id": user["id"],
            "username": user["username"],
            "role": user["role"],
            "nickname": user["nickname"],
        }
    )


@app.get("/api/v1/products")
def product_list():
    page = request.args.get("page", default="1")
    page_size = request.args.get("page_size", default="5")
    keyword = request.args.get("keyword", default="").strip().lower()

    try:
        page_num = int(page)
        size_num = int(page_size)
    except ValueError:
        return failure(10031, "page and page_size must be int", 400)

    if page_num <= 0 or size_num <= 0:
        return failure(10032, "page and page_size must be positive", 400)

    products = STATE["products"]
    if keyword:
        products = [
            item
            for item in products
            if keyword in item["name"].lower() or keyword in item["category"].lower()
        ]

    start = (page_num - 1) * size_num
    end = start + size_num
    page_items = products[start:end]

    return success(
        {
            "page": page_num,
            "page_size": size_num,
            "total": len(products),
            "items": page_items,
        }
    )


@app.get("/api/v1/products/<int:product_id>")
def product_detail(product_id: int):
    for item in STATE["products"]:
        if item["id"] == product_id:
            return success(item)
    return failure(10041, "product not found", 404)


@app.post("/api/v1/products")
def create_product():
    user = current_user()
    if not user:
        return failure(10051, "token required", 401)

    payload = request.get_json(silent=True)
    if not payload:
        return failure(10052, "json body required", 400)

    name = str(payload.get("name", "")).strip()
    category = str(payload.get("category", "")).strip()
    price = payload.get("price")

    if not name:
        return failure(10053, "name required", 400)
    if not category:
        return failure(10054, "category required", 400)
    if price is None:
        return failure(10055, "price required", 400)

    try:
        price = float(price)
    except (TypeError, ValueError):
        return failure(10056, "price must be number", 400)

    product = {
        "id": next_product_id(),
        "name": name,
        "category": category,
        "price": price,
        "created_by": user["username"],
    }
    STATE["products"].append(product)
    return success(product, status=201)


@app.delete("/api/v1/products/<int:product_id>")
def delete_product(product_id: int):
    user = current_user()
    if not user:
        return failure(10061, "token required", 401)

    for index, item in enumerate(STATE["products"]):
        if item["id"] == product_id:
            deleted = STATE["products"].pop(index)
            return success({"deleted": True, "product": deleted})
    return failure(10062, "product not found", 404)


@app.post("/api/v1/echo-form")
def echo_form():
    form_data = request.form.to_dict()
    if not form_data:
        return failure(10071, "form data required", 400)
    return success({"form": form_data})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
