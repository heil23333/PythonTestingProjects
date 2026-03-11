# 接口自动化测试够用的 Python 教程

## 1. 这份教程的定位

这不是完整 Python 教程。

它只覆盖你做接口自动化测试真正会用到的内容：

- 变量和数据类型
- 字符串、列表、字典
- `if`
- `for`
- 函数
- 模块导入
- 异常处理
- 读写 JSON
- 处理接口响应数据

如果一个知识点对你写 `requests`、`pytest`、接口断言没有直接帮助，这份教程就先不讲。

---

## 2. 变量

变量就是给一个值起名字。

```python
base_url = "http://127.0.0.1:5001"
username = "alice"
password = "123456"
status_code = 200
```

接口自动化里最常见的变量有：

- `base_url`
- `token`
- `headers`
- `params`
- `payload`
- `resp`

---

## 3. 常用数据类型

## 3.1 字符串 `str`

最常见。

```python
token = "token-1"
url = "http://127.0.0.1:5001/api/v1/login"
```

### 常用操作

```python
username = " alice "
print(username.strip())      # 去掉两端空格
print(username.lower())      # 转小写
print(username.upper())      # 转大写
```

### f-string

做接口自动化时非常常见。

```python
product_id = 7
url = f"http://127.0.0.1:5001/api/v1/products/{product_id}"
```

---

## 3.2 数字 `int` / `float`

```python
page = 1
page_size = 10
price = 199.0
```

接口里经常遇到：

- 页码
- 数量
- ID
- 价格

---

## 3.3 布尔值 `bool`

```python
is_login = True
is_deleted = False
```

常用于：

- 状态判断
- 断言逻辑

---

## 3.4 列表 `list`

列表就是一组有顺序的数据。

```python
ids = [1, 2, 3]
users = ["alice", "bob"]
```

接口响应里常见：

```python
items = resp.json()["data"]["items"]
print(items[0])
print(len(items))
```

---

## 3.5 字典 `dict`

字典是接口自动化里最重要的数据结构之一。

请求体、请求头、响应 JSON，很多时候都对应字典。

```python
headers = {"Authorization": "Bearer token-1"}
params = {"page": 1, "page_size": 3}
payload = {"username": "alice", "password": "123456"}
```

### 取值

```python
user = {"id": 1, "username": "alice"}

print(user["username"])
print(user.get("username"))
print(user.get("nickname"))
```

区别：

- `user["username"]`：键不存在会报错
- `user.get("username")`：键不存在返回 `None`

做接口测试时，`get()` 很常用。

---

## 4. 打印和调试

最基础但非常重要。

```python
print(resp.status_code)
print(resp.text)
print(resp.json())
```

如果你今天脚本跑不通，第一件事通常不是重写，而是先打印：

- 请求地址
- 请求参数
- 响应状态码
- 响应内容

---

## 5. 条件判断 `if`

很多断言前置逻辑都离不开它。

```python
status_code = 200

if status_code == 200:
    print("HTTP success")
else:
    print("HTTP failed")
```

接口场景示例：

```python
resp_json = resp.json()

if resp_json["code"] == 0:
    print("业务成功")
else:
    print("业务失败")
```

---

## 6. 循环 `for`

接口自动化里最常见的用途：

- 遍历响应列表
- 遍历测试数据

```python
items = resp.json()["data"]["items"]

for item in items:
    print(item["id"], item["name"])
```

你也会经常看到：

```python
cases = [
    {"username": "alice", "password": "123456"},
    {"username": "alice", "password": "wrong"},
]

for case in cases:
    print(case)
```

这其实就是后面 `pytest` 参数化的前置思维。

---

## 7. 函数

函数是把重复逻辑收起来。

### 7.1 最基础写法

```python
def add(a, b):
    return a + b
```

### 7.2 接口自动化场景

```python
def build_auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
```

调用：

```python
headers = build_auth_headers("token-1")
```

### 7.3 为什么重要

后面你会反复遇到重复逻辑：

- 构造请求头
- 登录获取 token
- 发送请求
- 读取配置

这些都适合慢慢抽成函数。

---

## 8. 模块导入

Python 文件之间靠 `import` 协作。

```python
import json
import requests
```

或者：

```python
from pathlib import Path
```

你现在先理解一件事：

- 标准库直接导
- 第三方库先安装再导
- 自己写的模块后面也可以导

---

## 9. 异常处理 `try/except`

做接口自动化时，经常会遇到：

- 响应不是 JSON
- 键不存在
- 类型不对

基础用法：

```python
try:
    data = resp.json()
    print(data["data"]["token"])
except Exception as e:
    print("解析失败:", e)
```

你现阶段不用追求写得很复杂，但要知道：

- 程序报错不可怕
- 关键是你要知道它为什么报错

---

## 10. 文件和 JSON

做接口自动化后面会经常接触 JSON 数据文件。

### 10.1 写 JSON

```python
import json

data = {"username": "alice", "password": "123456"}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### 10.2 读 JSON

```python
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["username"])
```

---

## 11. 处理接口响应的典型写法

下面这段代码你一定要看熟：

```python
import requests

resp = requests.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
)

print(resp.status_code)
print(resp.text)

resp_json = resp.json()
print(resp_json["code"])
print(resp_json["message"])
print(resp_json["data"]["token"])
```

这里同时用到了：

- 变量
- 字典
- 字符串
- JSON 解析

这就是你后面会最常写的代码形态。

---

## 12. 你现阶段最该会写的 Python 代码

如果你能熟练写下面这些，就足够支持接口自动化入门了：

```python
base_url = "http://127.0.0.1:5001"
login_url = f"{base_url}/api/v1/login"

payload = {"username": "alice", "password": "123456"}
headers = {"Content-Type": "application/json"}

if payload["username"] == "alice":
    print("username ok")

for key, value in payload.items():
    print(key, value)

def build_auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
```

---

## 13. 这份教程不要求你现在掌握什么

你现在可以先不深究这些：

- 复杂类设计
- 装饰器
- 生成器
- 多线程
- 元编程
- 数据结构和算法题

这些对你当前的接口自动化入门不是第一优先级。

---

## 14. 自测清单

看你自己是否已经达到“够用”标准：

- 我能写字典和列表
- 我能从字典里取值
- 我能写 `if`
- 我能写 `for`
- 我能写简单函数
- 我能导入模块
- 我能读取 JSON 响应中的字段
- 我能用 f-string 拼接 URL 或请求头

如果这些都可以，你就足够进入 Day 3。

---

## 15. 建议怎么用这份教程

不要单独背语法。

建议结合 Day 2 和 Day 3 的内容一起用：

1. 看到 Python 不熟的语法时，回来查这一份
2. 把里面示例直接自己打一遍
3. 再回到接口脚本和 `pytest` 用例里使用

这样效率最高。
