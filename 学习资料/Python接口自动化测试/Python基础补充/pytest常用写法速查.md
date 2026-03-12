# pytest 常用写法速查

## 1. 这份文档怎么用

这不是完整 `pytest` 教程，而是你写接口自动化测试时最常查的写法集合。

适合快速翻这些问题：

- `pytest` 怎么安装
- 测试文件怎么命名
- `assert` 怎么写
- 参数化怎么写
- fixture 怎么写
- `conftest.py` 怎么用
- `-k`、`-v`、`-s` 这些命令是什么意思

---

## 2. 安装和检查

安装：

```bash
pip install pytest
```

检查版本：

```bash
pytest --version
```

---

## 3. 最小测试

```python
def test_demo():
    assert 1 + 1 == 2
```

运行：

```bash
pytest -v
```

---

## 4. 命名规则

最常见规则：

- 文件名：`test_*.py`
- 函数名：`test_*`

例如：

```text
test_login.py
test_profile.py
```

```python
def test_login():
    ...
```

---

## 5. 最常见断言

```python
assert resp.status_code == 200
assert body["code"] == 0
assert body["message"] == "success"
assert body["data"] is not None
assert "token" in body["data"]
```

---

## 6. 参数化

### 6.1 多参数写法

```python
import pytest


@pytest.mark.parametrize(
    "username,password,expected_status",
    [
        ("alice", "123456", 200),
        ("alice", "wrong", 401),
        ("", "123456", 400),
    ],
)
def test_login(username, password, expected_status):
    ...
```

### 6.2 单参数对象写法

```python
import pytest


CASES = [
    {"username": "alice", "password": "123456"},
    {"username": "alice", "password": "wrong"},
]


@pytest.mark.parametrize("case", CASES)
def test_login(case):
    username = case["username"]
    password = case["password"]
```

### 6.3 核心记忆点

- `parametrize` 会让同一个测试函数跑多次
- 每组数据跑一次
- 按位置匹配参数

---

## 7. fixture

### 7.1 最小 fixture

```python
import pytest


@pytest.fixture
def login_token():
    return "token-1"
```

测试里直接用：

```python
def test_profile(login_token):
    assert login_token == "token-1"
```

### 7.2 fixture 依赖 fixture

```python
import pytest


@pytest.fixture
def reset_data():
    print("reset")


@pytest.fixture
def login_token(reset_data):
    return "token-1"
```

只要写进参数里，就会先执行依赖的 fixture。

### 7.3 fixture 返回值和副作用

- 有的 fixture 用 `return` 返回数据
- 有的 fixture 不需要返回值，只需要先做一步动作

例如：

```python
@pytest.fixture
def reset_data():
    requests.post(...)
```

这里重要的是“先执行 reset”，不是它返回什么。

---

## 8. conftest.py

`conftest.py` 用来放公共 fixture。

例如：

```python
import pytest


@pytest.fixture
def base_url():
    return "http://127.0.0.1:5001"
```

只要测试文件在这个目录或它的子目录里，就可以直接用。

### 记忆点

- 不需要导入 `conftest.py`
- 不需要在测试里 `from conftest import ...`
- `pytest` 会自动发现它

---

## 9. pytest.ini

一般手动创建。

最小示例：

```ini
[pytest]
addopts = -v
testpaths = .
python_files = test_*.py
python_functions = test_*
```

作用：

- 统一测试规则
- 统一默认参数

---

## 10. 类里的测试写法

```python
class TestUser:
    def test_profile(self, login_token):
        assert login_token is not None
```

### 记忆点

- 类名通常以 `Test` 开头更清晰
- 方法名仍然要 `test_` 开头
- fixture 一样能注入

---

## 11. 最常用命令

运行全部测试：

```bash
pytest
```

详细模式：

```bash
pytest -v
```

显示 `print`：

```bash
pytest -s
```

详细模式 + 显示 `print`：

```bash
pytest -s -v
```

运行单个文件：

```bash
pytest test_login.py
```

关键字筛选：

```bash
pytest -k login
```

---

## 12. `-k` 的含义

```bash
pytest -k health
```

表示：

- 跑名字里匹配 `health` 的测试

它匹配的不只是函数名，还会参考：

- 文件名
- 类名
- 函数名

例如：

```text
test_health.py::test_demo
```

也会被匹配到。

---

## 13. 最常见的接口测试结构

```python
import requests


def test_health():
    resp = requests.get("http://127.0.0.1:5001/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["data"]["status"] == "ok"
```

---

## 14. fixture + parametrize 组合写法

```python
import pytest
import requests


@pytest.fixture
def login_token():
    return "token-1"


@pytest.mark.parametrize(
    "page,page_size",
    [
        (1, 2),
        (1, 3),
        (2, 2),
    ],
)
def test_product_list(login_token, page, page_size):
    assert login_token is not None
```

### 记忆点

- fixture 和参数化参数可以同时出现在函数参数里
- `pytest` 会自动区分

---

## 15. 最常见报错和定位

### 15.1 `fixture 'xxx' not found`

先检查：

- `conftest.py` 是否在正确目录
- fixture 名字是否写对
- 当前 `pytest` 执行目录是否正确

### 15.2 测试没被发现

先检查：

- 文件名是不是 `test_*.py`
- 函数名是不是 `test_*`

### 15.3 `pytest: command not found`

说明：

- 没安装
- 或没激活 `.venv`

### 15.4 参数化报错

通常是：

- 参数名数量和数据数量对不上

---

## 16. 你当前阶段最常用的最小模板

```python
import pytest
import requests


@pytest.fixture
def base_url():
    return "http://127.0.0.1:5001"


def test_health(base_url):
    resp = requests.get(f"{base_url}/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
```

---

## 17. 建议怎么用这份文档

你现在最优先用熟这些：

- `assert`
- `parametrize`
- `fixture`
- `conftest.py`
- `pytest -v`
- `pytest -s -v`
- `pytest -k xxx`

先把这些掌握好，已经足够支撑接口自动化入门阶段。
