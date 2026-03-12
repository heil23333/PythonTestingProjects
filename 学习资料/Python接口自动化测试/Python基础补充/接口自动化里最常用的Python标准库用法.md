# 接口自动化里最常用的 Python 标准库用法

## 1. 这份文档的定位

这不是完整的 Python 标准库手册。

它只整理做接口自动化测试时最常见、最值得先掌握的标准库。

目标是让你在下面这些场景里知道该用什么：

- 读写测试数据文件
- 拼接文件路径
- 打印日志
- 生成时间、随机值、唯一 ID
- 复制测试数据
- 处理字符串和正则
- 读取环境变量

如果一个标准库在接口自动化里出现概率很低，这份文档就先不讲。

---

## 2. 最值得优先掌握的标准库

建议优先顺序：

1. `json`
2. `pathlib`
3. `os`
4. `time` / `datetime`
5. `logging`
6. `copy`
7. `uuid`
8. `re`

---

## 3. `json`

这是接口自动化里最常用的标准库之一。

你会在下面这些地方反复用到它：

- 读取 JSON 测试数据文件
- 保存响应结果
- 处理 JSON 字符串
- 理解 `requests` 里 `json=` 的本质

### 3.1 `json.load()`

从文件读取 JSON。

```python
import json

with open("data/login_cases.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

print(type(cases))
print(cases[0])
```

适用场景：

- 读取测试数据
- 读取配置文件

### 3.2 `json.dump()`

把 Python 对象写入 JSON 文件。

```python
import json

result = {
    "status_code": 200,
    "message": "success"
}

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
```

常用参数：

- `ensure_ascii=False`
  让中文正常写入
- `indent=2`
  让文件更易读

### 3.3 `json.loads()`

把 JSON 字符串转成 Python 对象。

```python
import json

text = '{"username": "alice", "password": "123456"}'
data = json.loads(text)

print(type(data))
print(data["username"])
```

### 3.4 `json.dumps()`

把 Python 对象转成 JSON 字符串。

```python
import json

data = {"username": "alice", "password": "123456"}
text = json.dumps(data, ensure_ascii=False)

print(type(text))
print(text)
```

### 3.5 最重要的记忆法

- `load / dump`：处理文件
- `loads / dumps`：处理字符串

### 3.6 在接口自动化里最常见的实际写法

```python
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "login_cases.json"
LOGIN_CASES = json.loads(DATA_FILE.read_text(encoding="utf-8"))
```

---

## 4. `pathlib`

`pathlib` 是现在很推荐的路径处理方式。

它比直接拼字符串路径更稳，也更清晰。

### 4.1 `Path`

```python
from pathlib import Path

path = Path("data/login_cases.json")
print(path)
```

### 4.2 拼接路径

```python
from pathlib import Path

data_file = Path("data") / "login_cases.json"
print(data_file)
```

这里的 `/` 不是除法，是路径拼接。

### 4.3 当前文件所在目录

```python
from pathlib import Path

current_dir = Path(__file__).resolve().parent
print(current_dir)
```

这是接口自动化里特别常见的写法。

### 4.4 读文件

```python
from pathlib import Path

text = Path("demo.txt").read_text(encoding="utf-8")
print(text)
```

### 4.5 写文件

```python
from pathlib import Path

Path("demo.txt").write_text("hello", encoding="utf-8")
```

### 4.6 判断文件是否存在

```python
from pathlib import Path

data_file = Path("data/login_cases.json")
print(data_file.exists())
```

### 4.7 为什么它重要

做接口自动化时你很常需要：

- 找测试数据文件
- 找配置文件
- 找报告输出目录

这些都很适合用 `pathlib`。

---

## 5. `os`

`os` 在接口自动化里最常见的用途不是系统编程，而是：

- 读取环境变量
- 处理目录

### 5.1 读取环境变量

```python
import os

base_url = os.getenv("BASE_URL")
print(base_url)
```

### 5.2 给环境变量设置默认值

```python
import os

base_url = os.getenv("BASE_URL", "http://127.0.0.1:5001")
```

这个写法很实用，因为环境变量没有配置时也不会直接报错。

### 5.3 获取当前工作目录

```python
import os

print(os.getcwd())
```

当你怀疑 `pytest` 是在错误目录执行时，这个很好用。

### 5.4 创建目录

```python
import os

os.makedirs("reports", exist_ok=True)
```

适用场景：

- 保存报告
- 保存导出结果

---

## 6. `time`

`time` 最常见的作用是做简单时间戳和等待。

### 6.1 获取时间戳

```python
import time

ts = int(time.time())
print(ts)
```

适用场景：

- 生成不重复测试数据
- 给文件命名

### 6.2 睡眠等待

```python
import time

time.sleep(1)
```

接口自动化里不要滥用，但偶尔调试时会用到。

### 6.3 一个常见用法

```python
import time

username = f"test_user_{int(time.time())}"
print(username)
```

---

## 7. `datetime`

如果你需要更清晰的日期时间格式，`datetime` 比 `time` 更适合。

### 7.1 获取当前时间

```python
from datetime import datetime

now = datetime.now()
print(now)
```

### 7.2 格式化时间

```python
from datetime import datetime

now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now_str)
```

### 7.3 常见格式化用途

- 日志时间
- 报告文件名
- 生成测试备注

例如：

```python
from datetime import datetime

file_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
```

---

## 8. `logging`

接口自动化项目后面一定会接触它。

你现在先掌握最基本的用法即可。

### 8.1 最基础写法

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("start request")
logging.error("request failed")
```

### 8.2 为什么不用全靠 `print`

`print` 适合临时调试，但日志更适合：

- 长期保留
- 分级输出
- 更像真实项目

### 8.3 接口测试里的常见日志内容

- 请求 URL
- 请求方法
- 请求参数
- 响应状态码
- 响应体

### 8.4 最小实用例子

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("login request start")
```

---

## 9. `copy`

这个库很适合处理测试数据复制。

### 9.1 `copy.copy()`

浅拷贝。

```python
import copy

data = {"username": "alice", "tags": [1, 2]}
new_data = copy.copy(data)
```

### 9.2 `copy.deepcopy()`

深拷贝。

```python
import copy

data = {"username": "alice", "tags": [1, 2]}
new_data = copy.deepcopy(data)
new_data["tags"].append(3)

print(data)
print(new_data)
```

### 9.3 为什么接口自动化里常用 `deepcopy`

因为你经常会：

- 先准备一份标准请求体
- 再基于它修改某个字段做异常测试

例如：

```python
import copy

base_payload = {
    "username": "alice",
    "password": "123456"
}

wrong_payload = copy.deepcopy(base_payload)
wrong_payload["password"] = "wrong"
```

这就是非常典型的场景。

---

## 10. `uuid`

适合生成唯一值，避免测试数据重复。

### 10.1 基本用法

```python
import uuid

value = str(uuid.uuid4())
print(value)
```

### 10.2 接口自动化里的常见用法

```python
import uuid

username = f"user_{uuid.uuid4().hex[:8]}"
print(username)
```

适用场景：

- 注册用户名
- 唯一订单备注
- 唯一测试标题

---

## 11. `re`

正则在接口自动化里不是每天都写，但经常会遇到：

- 提取字符串
- 校验格式
- 判断响应内容里是否包含某种模式

### 11.1 `re.search()`

```python
import re

text = "token=abc123"
match = re.search(r"token=(\w+)", text)

if match:
    print(match.group(1))
```

### 11.2 `re.match()`

从开头匹配。

```python
import re

text = "abc123"
print(bool(re.match(r"^[a-z]+\d+$", text)))
```

### 11.3 `re.findall()`

查找所有匹配项。

```python
import re

text = "id=1 id=2 id=3"
print(re.findall(r"id=(\d+)", text))
```

### 11.4 接口测试里的典型用途

- 校验手机号格式
- 校验邮箱格式
- 提取响应中的某段字符串

---

## 12. `collections`

不是最优先，但偶尔有用。

### 12.1 `defaultdict`

适合做分组统计。

```python
from collections import defaultdict

result = defaultdict(list)
result["passed"].append("test_login")
print(result)
```

### 12.2 `Counter`

适合做简单统计。

```python
from collections import Counter

codes = [200, 200, 404, 500]
print(Counter(codes))
```

适用场景：

- 统计状态码分布
- 统计测试结果数量

---

## 13. `itertools`

一般不是入门第一优先级，但参数组合测试里偶尔会用。

### 13.1 `product`

```python
from itertools import product

usernames = ["alice", ""]
passwords = ["123456", "wrong"]

for username, password in product(usernames, passwords):
    print(username, password)
```

适用场景：

- 快速生成参数组合
- 组合边界测试数据

---

## 14. 标准库在接口自动化里的实际分工

你可以先这样记：

- `json`
  处理测试数据和 JSON 字符串
- `pathlib`
  处理文件路径
- `os`
  处理环境变量和目录
- `time` / `datetime`
  处理时间和文件名
- `logging`
  打日志
- `copy`
  复制请求体
- `uuid`
  生成唯一测试数据
- `re`
  做格式判断和提取

---

## 15. 你当前阶段最值得先会的 5 个片段

### 15.1 读取测试数据文件

```python
import json
from pathlib import Path

data_file = Path(__file__).resolve().parent / "data" / "login_cases.json"
cases = json.loads(data_file.read_text(encoding="utf-8"))
```

### 15.2 读取环境变量

```python
import os

base_url = os.getenv("BASE_URL", "http://127.0.0.1:5001")
```

### 15.3 生成唯一用户名

```python
import uuid

username = f"user_{uuid.uuid4().hex[:8]}"
```

### 15.4 复制请求体做异常场景

```python
import copy

base_payload = {"username": "alice", "password": "123456"}
wrong_payload = copy.deepcopy(base_payload)
wrong_payload["password"] = "wrong"
```

### 15.5 打印日志

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("request start")
```

---

## 16. 当前阶段不需要死磕的标准库

你现在可以先不深究这些：

- `threading`
- `asyncio`
- `subprocess`
- `socket`
- `sqlite3`
- `http.server`

这些并不是做接口自动化入门的第一优先级。

---

## 17. 建议怎么使用这份文档

最有效的方式不是从头背到尾，而是：

1. 写测试时遇到不会的标准库，再回来查
2. 把这里的短代码自己打一遍
3. 再放回你的接口测试场景里用

你当前最优先掌握的是：

- `json`
- `pathlib`
- `logging`
- `copy`
- `os.getenv`

先把这五个用熟，已经能覆盖很多接口自动化场景。
