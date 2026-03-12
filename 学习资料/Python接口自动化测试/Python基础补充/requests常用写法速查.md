# requests 常用写法速查

## 1. 这份文档怎么用

这不是系统教程，而是速查表。

适合你在写接口自动化时遇到这些问题时快速翻：

- GET 怎么写
- POST 怎么写
- `params` / `json` / `data` 怎么区分
- 怎么带 `headers`
- 怎么拿 `status_code` / `text` / `json()`
- 怎么设置超时
- 怎么用 `Session`

---

## 2. 基础导入

```python
import requests
```

---

## 3. 最常见的 GET 请求

```python
resp = requests.get("http://127.0.0.1:5001/health")

print(resp.status_code)
print(resp.text)
print(resp.json())
```

适用场景：

- 健康检查
- 列表查询
- 详情查询

---

## 4. 带查询参数的 GET

```python
resp = requests.get(
    "http://127.0.0.1:5001/api/v1/products",
    params={"page": 1, "page_size": 3, "keyword": "mouse"},
)

print(resp.url)
print(resp.json())
```

### 记忆点

- `params` 会拼到 URL 后面
- 最适合查询接口

---

## 5. 最常见的 POST 请求

```python
resp = requests.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
)

print(resp.status_code)
print(resp.json())
```

适用场景：

- 登录
- 新增
- 修改

---

## 6. `json=` 的写法

```python
payload = {
    "username": "alice",
    "password": "123456",
}

resp = requests.post(url, json=payload)
```

### 记忆点

- `json=` 用于 JSON 请求体
- `requests` 会自动处理 `Content-Type: application/json`

---

## 7. `data=` 的写法

```python
resp = requests.post(
    "http://127.0.0.1:5001/api/v1/echo-form",
    data={"name": "alice", "city": "shanghai"},
)

print(resp.json())
```

### 记忆点

- `data=` 更适合表单数据
- 常见于 `x-www-form-urlencoded`

---

## 8. `params` / `json` / `data` 最短区分法

- `params`
  URL 查询参数
- `json`
  JSON 请求体
- `data`
  表单请求体

---

## 9. 带请求头

```python
headers = {"Authorization": "Bearer token-1"}

resp = requests.get(
    "http://127.0.0.1:5001/api/v1/profile",
    headers=headers,
)
```

最常见场景：

- token 鉴权
- 自定义 `Content-Type`

---

## 10. 带 token 的典型写法

```python
login_resp = requests.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
)

token = login_resp.json()["data"]["token"]
headers = {"Authorization": f"Bearer {token}"}

profile_resp = requests.get(
    "http://127.0.0.1:5001/api/v1/profile",
    headers=headers,
)
```

---

## 11. DELETE 请求

```python
resp = requests.delete(
    "http://127.0.0.1:5001/api/v1/products/1",
    headers={"Authorization": "Bearer token-1"},
)

print(resp.status_code)
print(resp.json())
```

适用场景：

- 删除数据

---

## 12. 超时参数

```python
resp = requests.get(url, timeout=5)
```

### 建议

写接口测试时尽量都加 `timeout`，避免请求卡死。

---

## 13. 读取响应最常见的 3 个属性

### 13.1 `resp.status_code`

拿 HTTP 状态码。

```python
print(resp.status_code)
```

### 13.2 `resp.text`

拿原始响应文本。

```python
print(resp.text)
```

### 13.3 `resp.json()`

把 JSON 响应解析成 Python 对象。

```python
body = resp.json()
print(body["code"])
```

---

## 14. `resp.text` 和 `resp.json()` 的区别

- `resp.text`
  原始字符串
- `resp.json()`
  解析后的 Python 对象

如果响应不是 JSON，`resp.json()` 可能报错。

稳一点的写法：

```python
try:
    body = resp.json()
except ValueError:
    body = None
```

---

## 15. 常见断言写法

```python
body = resp.json()

assert resp.status_code == 200
assert body["code"] == 0
assert body["message"] == "success"
```

---

## 16. Session 的基本用法

```python
session = requests.Session()

login_resp = session.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
)

profile_resp = session.get("http://127.0.0.1:5001/api/v1/profile")
```

### 记忆点

- `Session` 可以复用连接
- 有些系统会依赖会话状态

你当前这套练习服务主要用 token，不强依赖 `Session`，但你要知道它的存在。

---

## 17. 最常见的链路写法

```python
import requests

BASE_URL = "http://127.0.0.1:5001"

login_resp = requests.post(
    f"{BASE_URL}/api/v1/login",
    json={"username": "alice", "password": "123456"},
    timeout=5,
)
login_body = login_resp.json()

token = login_body["data"]["token"]
headers = {"Authorization": f"Bearer {token}"}

create_resp = requests.post(
    f"{BASE_URL}/api/v1/products",
    headers=headers,
    json={"name": "Desk Lamp", "category": "lighting", "price": 199},
    timeout=5,
)
create_body = create_resp.json()

product_id = create_body["data"]["id"]

detail_resp = requests.get(
    f"{BASE_URL}/api/v1/products/{product_id}",
    timeout=5,
)

print(detail_resp.json())
```

---

## 18. 常见错误

### 18.1 用错 `params/json/data`

最常见。

判断方法：

- 查询 -> `params`
- JSON 请求体 -> `json`
- 表单 -> `data`

### 18.2 忘记带 token

受保护接口常见错误。

### 18.3 忘记加 timeout

请求出问题时可能会卡住。

### 18.4 直接 `resp.json()` 但响应不是 JSON

路由错误或服务异常时很常见。

---

## 19. 你当前阶段最常用的最小模板

```python
import requests

BASE_URL = "http://127.0.0.1:5001"


def test_demo():
    resp = requests.get(f"{BASE_URL}/health", timeout=5)
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
```

---

## 20. 建议怎么用这份文档

你现在最优先记住这些：

- `requests.get/post/delete`
- `params/json/data`
- `headers`
- `timeout`
- `resp.status_code`
- `resp.text`
- `resp.json()`

先把这些用熟，已经能覆盖大部分接口自动化入门场景。
