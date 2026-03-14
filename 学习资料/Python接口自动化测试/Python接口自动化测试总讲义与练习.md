# Python接口自动化测试总讲义与练习

## 1. 讲义与练习定位

这份讲义与练习不是“题目清单”，而是配合这本教材一起使用的训练手册：

[Python接口自动化测试完整教材.md](/Users/Apple/Documents/Codes/PythonTestingProjects/学习资料/Python接口自动化测试/Python接口自动化测试完整教材.md)

你可以把它理解成：

- 教材负责讲概念、讲顺序、讲为什么
- 讲义与练习负责让你输出、动手、检查自己是否真的学会

这份讲义与练习按“从完全入门到能做完整小项目”的顺序往下走，不建议跳着做。

---

## 2. 这份讲义与练习怎么用

每一章建议按下面顺序完成：

1. 先看教材对应章节
2. 再做本章热身题
3. 再做主练习
4. 再做实操任务
5. 最后看本章过关标准

你每做完一章，最好都留下这 3 类产物：

1. 一份文字答案
2. 一份操作记录
3. 一份自己的复盘

如果你只在脑子里想一遍，效果会差很多。

---

## 3. 做练习时的统一要求

### 3.1 文字题要求

如果题目要求“解释”“回答”“说明”，默认按下面标准写：

1. 先写结论
2. 再写原因
3. 最后举例

### 3.2 实操题要求

如果题目要求“手工调接口”或“写代码”，默认至少记录：

1. 你操作了什么
2. 你看到了什么结果
3. 你怎么判断结果是否正确

### 3.3 复盘要求

每一章最后都建议写 3 句话：

1. 这一章我真正学会了什么
2. 我还不够稳的地方是什么
3. 下一次再做，我最容易错在哪里

---

## 4. 建议你准备一个固定练习区

为了让这份讲义与练习真的能用，建议你给自己固定 3 个记录区：

1. 概念笔记区
2. 实操记录区
3. 错题复盘区

你可以自己建一个 Markdown 文件，例如：

```text
学习记录/
├── 01_概念笔记.md
├── 02_实操记录.md
└── 03_错题复盘.md
```

这不是形式主义，而是为了让你能看到自己在进步。

---

## 5. 模块一：接口与接口测试基础

### 5.1 本模块目标

做完这一章，你应该做到：

1. 能用自己的话解释接口是什么
2. 能解释接口测试和页面测试的区别
3. 能说出接口测试至少测哪几类内容
4. 不再把接口测试理解成“只测成功场景”

### 5.2 热身题

请不要看教材，直接回答：

1. 什么是接口？
2. 什么是接口测试？
3. 接口测试和 UI 测试最大的区别是什么？
4. 你觉得接口测试的价值是什么？

### 5.3 主练习一：用自己的话解释概念

请分别写 80 到 150 字回答下面两个问题：

#### 题目 1

如果有人问你“接口是什么”，你怎么解释？

#### 题目 2

如果有人问你“接口测试是做什么的”，你怎么解释？

### 5.4 主练习二：区分“会调接口”和“会做接口测试”

请判断下面哪种说法更像“会调接口”，哪种更像“会做接口测试”，并写原因。

#### 说法 A

“我能把登录接口调通，拿到返回结果。”

#### 说法 B

“我会验证登录接口的成功、失败、空值、用户不存在、权限和异常场景。”

### 5.5 主练习三：登录接口测试点设计

假设有一个登录接口，请你至少写出 10 个测试点。

要求至少覆盖：

1. 正常场景
2. 参数为空
3. 参数错误
4. 用户不存在
5. 密码错误
6. 安全或鉴权相关

#### 输出模板

你可以按下面模板写：

```text
1. 测试点名称：
   输入：
   预期：

2. 测试点名称：
   输入：
   预期：
```

### 5.6 实操任务

选择一个你能访问的接口（公开接口或本地接口都可以），完成下面动作：

1. 找到接口地址
2. 确认请求方法
3. 确认请求参数
4. 记录一个成功响应
5. 记录一个失败响应

#### 实操记录模板

```text
接口名称：
接口地址：
请求方法：
是否需要登录：
请求参数：
成功响应：
失败响应：
我认为这个接口至少有哪 5 个测试点：
```

### 5.7 过关标准

做完这一章，如果你已经能做到下面这些，就算过关：

- 能口头解释“接口”和“接口测试”
- 能说出接口测试不只测成功
- 能独立写出登录接口的基础测试点

### 5.8 复盘题

请写下这 3 句话：

1. 我过去对接口测试最容易误解的是什么？
2. 现在我对接口测试的理解有什么变化？
3. 这一章我最不确定的概念是什么？

---

## 6. 模块二：HTTP、URL、请求与响应

### 6.1 本模块目标

做完这一章，你应该做到：

1. 能看懂一个请求的基本组成
2. 能解释 URL、方法、请求头、参数、请求体
3. 能解释响应状态码和响应体
4. 能区分 HTTP 层结果和业务层结果

### 6.2 热身题

请不看教材，先回答：

1. `GET` 和 `POST` 的区别是什么？
2. URL 是什么？
3. 状态码 `404` 代表什么？
4. 响应体和状态码有什么区别？

### 6.3 主练习一：拆一个请求

请看下面这个请求，拆出它的每一个组成部分：

```text
POST http://127.0.0.1:5001/api/v1/login
Headers:
Content-Type: application/json

Body:
{
  "username": "alice",
  "password": "123456"
}
```

#### 你需要回答

1. URL 是什么？
2. 请求方法是什么？
3. 请求头是什么？
4. 请求体是什么？
5. 这类请求通常用在什么场景？

### 6.4 主练习二：拆一个响应

请看下面这个响应，拆出它的每个部分并解释：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "token": "token-1"
  }
}
```

同时假设 HTTP 状态码为 `200`。

#### 你需要回答

1. 状态码代表什么？
2. `code` 代表什么？
3. `message` 代表什么？
4. `data` 代表什么？
5. 为什么说不能只断言 `200`？

### 6.5 主练习三：判断题

请判断下面说法对不对，并写原因。

1. `GET` 一定不带参数。
2. `POST` 一定表示新增。
3. `404` 一定表示接口地址写错。
4. HTTP 状态码 `200` 就表示业务一定成功。
5. 接口返回 JSON 时，测试只需要看 `data`。

### 6.6 主练习四：状态码理解

请分别写出下面这些状态码在接口测试里通常怎么理解：

- `200`
- `201`
- `400`
- `401`
- `403`
- `404`
- `500`

并补充一个问题：

“资源不存在型 `404`” 和 “路由不存在型 `404`” 的区别是什么？

### 6.7 实操任务

用你当前的接口环境，任选 2 个接口，完成下面表格。

#### 记录模板

```text
接口 1：
URL：
方法：
请求头：
请求参数：
请求体：
状态码：
响应体：
我对这个响应的理解：

接口 2：
URL：
方法：
请求头：
请求参数：
请求体：
状态码：
响应体：
我对这个响应的理解：
```

### 6.8 过关标准

做完这一章后，你应该能看着一个请求说清楚：

- 发到哪里
- 用什么方法
- 带了什么
- 回了什么

### 6.9 复盘题

1. 我以前是不是只盯着状态码？
2. 我现在能不能区分状态码和业务码？
3. 我对哪一种状态码最容易误解？

---

## 7. 模块三：`params`、`json`、`data`、`headers`

### 7.1 本模块目标

做完这一章，你应该做到：

1. 知道 `params/json/data` 的区别
2. 能根据接口场景判断该优先用哪种传参方式
3. 知道请求头通常有什么作用
4. 不会再把所有参数都乱塞进一个地方

### 7.2 热身题

请先直接回答：

1. `params` 放哪里？
2. `json` 发的是什么格式？
3. `data` 通常什么时候用？
4. `headers` 最常见有什么用？

### 7.3 主练习一：分类题

下面这些场景，你会优先选择 `params`、`json` 还是 `data`？

1. 商品列表分页查询
2. 用户登录
3. 表单提交
4. 商品详情查询
5. 新增商品
6. 搜索接口关键字查询
7. 修改密码

#### 输出模板

```text
1. 场景：
   我选：
   原因：
```

### 7.4 主练习二：改错题

请指出下面写法的问题，并改成更合理的方式。

#### 题目 1

```python
requests.get(url, json={"page": 1, "page_size": 10})
```

#### 题目 2

```python
requests.post(url, params={"username": "alice", "password": "123456"})
```

#### 题目 3

接口文档要求 `application/x-www-form-urlencoded`，你却写了：

```python
requests.post(url, json={"name": "alice"})
```

### 7.5 主练习三：解释题

请解释：

为什么“传的是字典”不等于“`json` 和 `data` 没区别”？

### 7.6 主练习四：请求头理解

请解释下面这些请求头最常见的用途：

```python
Content-Type: application/json
Authorization: Bearer token-1
```

### 7.7 实操任务

请你至少实际调 3 种不同形式的请求：

1. 带 `params` 的 GET
2. 带 `json` 的 POST
3. 带 `headers` 的鉴权请求

#### 记录模板

```text
请求 1：
方法：
传参方式：
实际传了什么：
状态码：
响应体：

请求 2：
方法：
传参方式：
实际传了什么：
状态码：
响应体：

请求 3：
方法：
传参方式：
实际传了什么：
状态码：
响应体：
```

### 7.8 过关标准

如果你已经能做到下面这些，就算过关：

- 看场景能大致判断该用 `params/json/data`
- 知道请求头不只是装饰
- 能解释为什么登录通常用 `json`

### 7.9 复盘题

1. 我最容易把哪两种传参方式混掉？
2. 我现在是否知道“该看接口文档判断怎么传”？
3. 哪种请求头我还不熟？

---

## 8. 模块四：响应处理与错误判断

### 8.1 本模块目标

做完这一章，你应该做到：

1. 能区分 `resp.text` 和 `resp.json()`
2. 知道什么时候 `resp.json()` 会报错
3. 能理解 JSON 里的 `null` 和“不是 JSON”不是一回事
4. 能区分“业务失败”和“路由失败”

### 8.2 热身题

请先回答：

1. `resp.text` 是什么？
2. `resp.json()` 是什么？
3. 状态码不是 200 时，能不能 `resp.json()`？

### 8.3 主练习一：概念题

请分别解释下面两个表达式拿到的内容是什么：

```python
resp.text
resp.json()
```

并补充：

它们最适合用在哪些场景？

### 8.4 主练习二：判断题

请判断下面情况能不能直接 `resp.json()`。

#### 情况 1

```json
{"code":10013,"message":"user not found","data":null}
```

#### 情况 2

```html
<html><body>404 Not Found</body></html>
```

#### 情况 3

响应体为空

#### 情况 4

```json
{"code":0,"message":"success","data":{"status":"ok"}}
```

### 8.5 主练习三：解释题

请你用自己的话解释：

为什么下面这个响应里 `data` 是 `null`，但 `resp.json()` 仍然可以正常用？

```json
{"code":10013,"message":"user not found","data":null}
```

### 8.6 主练习四：场景区分

请解释下面两个场景的区别：

1. `/api/v1/products/9999`
2. `/api/v1/productssss/9999`

你需要回答：

- 哪个更像资源不存在
- 哪个更像路由不存在
- 哪个更适合直接 `resp.json()`

### 8.7 实操任务

请你至少找 2 个失败响应，记录：

1. 状态码
2. `resp.text`
3. 是否能 `resp.json()`
4. 为什么

### 8.8 过关标准

做完这一章，你应该能不再把下面几件事混掉：

- JSON 字段值是 `null`
- 响应体不是 JSON
- 业务型 404
- 路由型 404

### 8.9 复盘题

1. 我以前是不是把 `404` 都理解成 URL 错？
2. 我现在能不能解释为什么 `data: null` 不影响 `resp.json()`？
3. 我排查响应问题时，应该先看什么？

---

## 9. 模块五：鉴权、Token、接口文档阅读

### 9.1 本模块目标

做完这一章，你应该做到：

1. 能解释 Cookie、Session、Token、JWT 的基本区别
2. 知道接口自动化里最常见的鉴权方式是什么
3. 能从接口文档里找出是否需要登录
4. 能看出一个接口调用前是否依赖前置请求

### 9.2 热身题

请先回答：

1. Token 是什么？
2. JWT 和 Token 是不是完全一样？
3. 为什么资料接口通常要先登录？
4. 接口文档里哪些地方最值得看？

### 9.3 主练习一：概念理解

请分别写 50 到 100 字解释：

1. Cookie
2. Session
3. Token
4. JWT

要求：

- 不追求官方定义
- 用你自己能听懂的语言解释

### 9.4 主练习二：接口文档阅读

请找一个需要登录的接口，按照下面模板拆解：

```text
接口名称：
接口地址：
请求方法：
是否需要登录：
token 放在哪：
请求参数：
成功响应：
失败响应：
调用它之前，我需要先做什么：
```

### 9.5 主练习三：接口关联思路题

假设你有下面 3 个接口：

1. 登录接口
2. 查询个人资料接口
3. 新增商品接口

请你写出一条可能的测试链路，并说明：

1. 哪一步是前置请求
2. 哪一步依赖 token
3. 哪一步依赖前一步的返回值

### 9.6 主练习四：请求头解释

请解释下面这段代码的含义：

```python
headers = {"Authorization": f"Bearer {token}"}
```

### 9.7 实操任务

请至少完成一条完整鉴权链路：

1. 登录拿 token
2. 带 token 访问一个需要鉴权的接口

并记录：

```text
登录请求：
登录响应：
拿到的 token：
后续请求：
后续响应：
```

### 9.8 过关标准

做完这一章，你应该能解释：

- 为什么要先登录
- token 一般怎么传
- 什么叫前置请求

### 9.9 复盘题

1. 我以前是不是把 token 理解得太抽象？
2. 我现在能不能讲清登录和资料接口的关系？
3. 我读接口文档时最容易漏掉哪块？

---

## 10. 模块六：Python 最小够用基础

### 10.1 本模块目标

做完这一章，你应该做到：

1. 能看懂接口自动化中常见的 Python 代码
2. 能操作字符串、列表、字典
3. 能看懂 `f-string`
4. 能理解 `json` 模块和 `pathlib` 的基础用法

### 10.2 热身题

请先回答：

1. 字典为什么在接口自动化里特别重要？
2. 列表最常出现在哪？
3. `f"Bearer {token}"` 里的 `f` 是干什么的？

### 10.3 主练习一：数据类型识别

请判断下面每个值在 Python 里是什么类型：

```python
"alice"
123
199.0
True
[1, 2, 3]
{"username": "alice"}
```

### 10.4 主练习二：字典取值

已知：

```python
body = {
    "code": 0,
    "message": "success",
    "data": {
        "user": {
            "username": "alice"
        }
    }
}
```

请写出如何取到：

1. `code`
2. `message`
3. `username`

### 10.5 主练习三：`f-string`

已知：

```python
token = "token-1"
product_id = 7
```

请写出：

1. `Authorization` 请求头
2. 商品详情接口 URL

### 10.6 主练习四：路径题

请解释下面代码的意思：

```python
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "login_cases.json"
```

要求你说清楚：

1. `__file__` 是什么
2. `resolve()` 的作用是什么
3. `.parent.parent` 在做什么
4. 为什么用 `/` 连接路径

### 10.7 主练习五：`json` 模块

请解释下面 4 个函数的区别：

1. `json.loads()`
2. `json.dumps()`
3. `json.load()`
4. `json.dump()`

并回答：

如果 JSON 文件内容是数组，读进 Python 后通常是什么类型？

### 10.8 实操任务

请自己写一份最小 Python 练习代码，要求包含：

1. 一个字典
2. 一个列表
3. 一个 `f-string`
4. 一次 JSON 文件读取

### 10.9 过关标准

做完这一章，你应该能支撑后面阅读：

- 请求体
- headers
- 测试数据
- fixture
- 路径代码

### 10.10 复盘题

1. 我最容易在哪个 Python 基础点卡住？
2. 我现在能不能看懂简单的接口测试代码？
3. 哪个标准库我还需要回去再补？

---

## 11. 模块七：用 `requests` 把手工操作变成代码

### 11.1 本模块目标

做完这一章，你应该做到：

1. 能用 `requests` 发 GET、POST、DELETE 请求
2. 能把手工调接口转成 Python 代码
3. 能打印状态码和响应体做基础排查
4. 能理解为什么当前阶段先不过度封装

### 11.2 热身题

1. `requests.get()` 和 `requests.post()` 分别适合什么场景？
2. 为什么 Day 2 不建议一上来就写很复杂的框架？

### 11.2.1 先看一套完整范例

这一章不要只做题，先把下面这套完整范例看懂。

```python
import requests

BASE_URL = "http://127.0.0.1:5001"


login_resp = requests.post(
    f"{BASE_URL}/api/v1/login",
    json={"username": "alice", "password": "123456"},
    timeout=5,
)
print(login_resp.status_code)
print(login_resp.text)

login_body = login_resp.json()
token = login_body["data"]["token"]

profile_resp = requests.get(
    f"{BASE_URL}/api/v1/profile",
    headers={"Authorization": f"Bearer {token}"},
    timeout=5,
)
print(profile_resp.status_code)
print(profile_resp.text)
```

你现在先不要急着背语法，而是先把这段拆成 4 步：

1. 先登录
2. 看登录响应
3. 提取 token
4. 带 token 查资料

如果你能把这 4 步用自己的话说出来，再去做下面练习，会顺很多。

### 11.3 主练习一：最小请求代码

请分别写出下面 4 类请求的最小代码：

1. 健康检查
2. 登录
3. 商品列表查询
4. 商品详情查询

#### 参考写法骨架

你可以先按下面骨架补全：

```python
import requests

BASE_URL = "http://127.0.0.1:5001"


def request_health():
    resp = requests.get(f"{BASE_URL}/health", timeout=5)
    print(resp.status_code)
    print(resp.text)


def request_login():
    resp = requests.post(
        f"{BASE_URL}/api/v1/login",
        json={"username": "alice", "password": "123456"},
        timeout=5,
    )
    print(resp.status_code)
    print(resp.text)


def request_product_list():
    resp = requests.get(
        f"{BASE_URL}/api/v1/products",
        params={"page": 1, "page_size": 5},
        timeout=5,
    )
    print(resp.status_code)
    print(resp.text)


def request_product_detail():
    resp = requests.get(f"{BASE_URL}/api/v1/products/1", timeout=5)
    print(resp.status_code)
    print(resp.text)
```

这里你要重点观察：

- 健康检查是最小 GET
- 登录是 POST + `json=`
- 商品列表是 GET + `params=`
- 商品详情是路径参数

### 11.4 主练习二：观察输出

对每条请求，至少打印：

```python
print(resp.status_code)
print(resp.text)
```

然后写出你观察到的内容：

1. 状态码是多少
2. 响应体长什么样
3. 能不能继续 `resp.json()`

### 11.5 主练习三：登录链路

请把下面链路变成代码：

1. 登录
2. 拿 token
3. 带 token 查资料

### 11.6 实操任务

请至少独立完成下面这个最小闭环：

1. 发送一个 GET 请求
2. 发送一个 POST 请求
3. 拿返回数据中的一个字段
4. 把它用到下一条请求中

#### 建议你按这个顺序做

1. 先写登录请求
2. 打印 `status_code` 和 `text`
3. 再写 `login_body = login_resp.json()`
4. 提取 `token`
5. 再写资料查询请求

#### 闭环范例

```python
import requests

BASE_URL = "http://127.0.0.1:5001"


login_resp = requests.post(
    f"{BASE_URL}/api/v1/login",
    json={"username": "alice", "password": "123456"},
    timeout=5,
)
print(login_resp.status_code)
print(login_resp.text)

login_body = login_resp.json()
token = login_body["data"]["token"]

profile_resp = requests.get(
    f"{BASE_URL}/api/v1/profile",
    headers={"Authorization": f"Bearer {token}"},
    timeout=5,
)
print(profile_resp.status_code)
print(profile_resp.text)
```

### 11.7 输出模板

```text
请求 1 做了什么：
请求 1 的结果：
我从请求 1 里拿到了什么：
请求 2 做了什么：
请求 2 的结果：
```

### 11.8 过关标准

如果你已经能不借助 Postman，靠 Python 调通基础接口，就算这一章过关。

### 11.9 复盘题

1. 我最容易在哪一步写错请求？
2. 我排查问题时，会不会先打印状态码和响应体？
3. 我是否已经能把手工调接口改成代码？

---

## 12. 模块八：从脚本升级到 `pytest` 测试

### 12.1 本模块目标

做完这一章，你应该做到：

1. 明白脚本和测试的区别
2. 会写最基础的 `pytest` 测试函数
3. 会写基础断言
4. 会使用最常见的 `pytest` 命令

### 12.2 热身题

1. 为什么下面这段更像脚本而不像测试？

```python
resp = requests.get(url)
print(resp.json())
```

2. 一个真正的测试至少应该多出什么？

### 12.2.1 先看“脚本”和“测试”的对照范例

#### 只是脚本

```python
import requests

resp = requests.get("http://127.0.0.1:5001/health")
print(resp.status_code)
print(resp.text)
```

#### 真正的测试

```python
import requests


def test_health():
    resp = requests.get("http://127.0.0.1:5001/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
```

请你自己比较这两段代码到底差在哪里。

你最少要能说出这 3 点：

1. 第二段有 `test_` 开头的测试函数
2. 第二段有自动断言
3. 第二段可以直接交给 `pytest` 执行

### 12.3 主练习一：改造成测试

请把下面脚本改成真正的测试：

```python
resp = requests.get("http://127.0.0.1:5001/health")
print(resp.status_code)
print(resp.json())
```

要求至少包含：

1. 一条状态码断言
2. 一条业务字段断言

#### 参考答案形态

你最后至少应该写成接近下面这样：

```python
import requests


def test_health():
    resp = requests.get("http://127.0.0.1:5001/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
```

### 12.4 主练习二：命令理解

请解释下面命令分别做什么：

```bash
pytest
pytest -v
pytest -s -v
pytest -k login
```

### 12.5 主练习三：筛选理解

请回答：

1. `pytest -k health` 是只匹配函数名吗？
2. 如果文件名里有 `health`，函数名不带，会不会被选中？

### 12.6 实操任务

请至少写出两条最小测试：

1. 健康检查测试
2. 商品详情测试

#### 建议范例

```python
import requests

BASE_URL = "http://127.0.0.1:5001"


def test_health():
    resp = requests.get(f"{BASE_URL}/health", timeout=5)
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0


def test_product_detail():
    resp = requests.get(f"{BASE_URL}/api/v1/products/1", timeout=5)
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["data"]["id"] == 1
```

#### 建议运行命令

```bash
pytest -s -v
```

如果你想只跑这两条，可以用：

```bash
pytest -k "health or product_detail" -s -v
```

### 12.7 过关标准

做完这一章，你应该能区分：

- 只是写请求脚本
- 真正写测试用例

### 12.8 复盘题

1. 我会不会还在“写脚本”的思路里？
2. 我现在是否知道测试至少要有断言？
3. 我最常用的 `pytest` 命令是哪几条？

---

## 13. 模块九：参数化、fixture、`conftest.py`

### 13.1 本模块目标

做完这一章，你应该做到：

1. 能解释参数化的作用
2. 能写出参数化登录测试
3. 能理解 fixture 的作用
4. 能理解 `conftest.py` 的自动发现机制
5. 能理解 fixture 之间的依赖

### 13.2 热身题

请回答：

1. 参数化解决什么问题？
2. fixture 解决什么问题？
3. 为什么 `conftest.py` 不需要手动导入？

### 13.3 主练习一：参数化阅读题

请解释下面代码每一部分的含义：

```python
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

你需要说清楚：

1. 参数是怎么按位置匹配的
2. 这段代码会执行几次
3. 每次执行时传的是什么值

### 13.4 主练习二：fixture 理解题

请解释下面代码：

```python
@pytest.fixture
def reset_data():
    ...


@pytest.fixture
def login_token(reset_data):
    ...
```

重点回答：

1. 为什么 `reset_data` 会先执行
2. 为什么即使 `login_token` 函数体里没用 `reset_data`，它也依然有意义

### 13.5 主练习三：组合题

请解释为什么下面的测试能同时用 fixture 和参数化：

```python
@pytest.mark.parametrize("case", LOGIN_CASES)
def test_login(auth_headers, case):
    ...
```

### 13.6 主练习四：`pytest.ini` 和 `conftest.py`

请回答：

1. `pytest.ini` 需要手动创建吗？
2. 不创建 `pytest.ini` 时，`conftest.py` 还会不会被自动发现？
3. `conftest.py` 放在根目录和放在子目录，作用范围有什么不同？

### 13.7 实操任务

请自己完成下面这些：

1. 写一个登录参数化测试
2. 写一个 `reset_data` fixture
3. 写一个 `login_token` fixture
4. 写一个 `auth_headers` fixture

### 13.8 输出模板

```text
我一共写了哪些 fixture：
每个 fixture 的作用：
参数化里一共准备了几组数据：
每组数据分别在测什么：
```

### 13.9 过关标准

做完这一章，你应该已经具备基础接口自动化测试结构能力。

### 13.10 复盘题

1. 我最容易把哪两个概念混掉？参数化和 fixture？fixture 和普通函数？
2. 我现在能不能解释“为什么 `conftest.py` 不用导入”？
3. 我能不能写出一条登录参数化测试？

---

## 14. 模块十：项目结构、配置、公共请求入口

### 14.1 本模块目标

做完这一章，你应该做到：

1. 能解释为什么代码要分层
2. 知道 `config/`、`common/`、`data/`、`testcases/` 放什么
3. 知道这些文件放好以后怎么导入、怎么调用
4. 能理解为什么不能只堆目录而不讲使用方式

### 14.2 热身题

请回答：

1. 为什么 Day 5 不只是“建几个文件夹”？
2. 为什么配置应该先迁到 `config/`？
3. 为什么 `send_request()` 不应该在每个文件都重复写？

### 14.2.1 先看一套完整项目范例

这一章一定不要只停留在“记目录名”，先看完整结构：

```text
api_auto_test/
├── config/
│   └── settings.py
├── common/
│   ├── request_handler.py
│   ├── assert_util.py
│   └── logger.py
├── data/
│   ├── login_cases.json
│   └── product_cases.json
├── testcases/
│   ├── test_health.py
│   ├── test_login.py
│   ├── test_profile.py
│   └── test_product_flow.py
├── conftest.py
└── pytest.ini
```

这套结构不是为了“显得专业”，而是为了把职责拆开：

- 配置归配置
- 公共能力归公共能力
- 数据归数据
- 测试归测试

你后面做主练习时，就按这套结构去理解。

### 14.3 主练习一：目录作用题

请分别解释下面目录和文件的作用：

- `config/settings.py`
- `common/request_handler.py`
- `common/assert_util.py`
- `common/logger.py`
- `data/login_cases.json`
- `testcases/test_login.py`
- `conftest.py`
- `pytest.ini`

#### 配套说明范例

做这道题时，不要只写“放配置”“放测试”，太薄了。建议按下面这种粒度写：

```text
config/settings.py
作用：放 BASE_URL、TIMEOUT、账号密码
这样放的效果：改环境信息时不用改测试逻辑
放好以后怎么用：from config.settings import BASE_URL, TIMEOUT
```

### 14.4 主练习二：导入方式题

请回答下面这些问题：

1. 如果是 `config.py`，你怎么导入？
2. 如果是 `config/settings.py`，你怎么导入？
3. 为什么导入写的是模块路径，不是文件系统路径？

### 14.5 主练习三：`send_request` 理解题

请解释下面代码：

```python
def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    return requests.request(method=method, url=url, **kwargs)
```

要求你说清楚：

1. `**kwargs` 是什么
2. `setdefault()` 在干什么
3. 为什么这里统一了请求入口
4. 这段代码解决了什么重复问题

#### 完整范例

`common/request_handler.py`

```python
import requests

from config.settings import TIMEOUT


def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    return requests.request(method=method, url=url, **kwargs)
```

#### 这个函数在测试里怎么用

`testcases/test_health.py`

```python
from common.request_handler import send_request
from config.settings import BASE_URL


def test_health():
    resp = send_request("GET", f"{BASE_URL}/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
```

这里你就能直接看到“封装前后”的区别：

- 封装前：每个文件都直接写 `requests.get(..., timeout=5)`
- 封装后：统一用 `send_request(...)`

### 14.6 主练习四：配置依赖顺序题

请解释：

为什么 Day 5 的学习顺序应该是：

1. 先配置
2. 再公共请求
3. 再断言和数据
4. 最后再测试文件

### 14.7 实操任务

请你自己画出当前项目结构，并在每一层后面写一句“这样放的效果”。

#### 输出模板

```text
config/：
作用：
这样放的效果：
放好以后怎么用：

common/：
作用：
这样放的效果：
放好以后怎么用：
```

#### 参考范例项目

如果你现在对“放完以后怎么写”还是不够稳，可以先对照下面这套最小成品。

`config/settings.py`

```python
BASE_URL = "http://127.0.0.1:5001"
TIMEOUT = 5
USERNAME = "alice"
PASSWORD = "123456"
```

`common/request_handler.py`

```python
import requests

from config.settings import TIMEOUT


def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    return requests.request(method=method, url=url, **kwargs)
```

`conftest.py`

```python
import pytest

from common.request_handler import send_request
from config.settings import BASE_URL, USERNAME, PASSWORD


@pytest.fixture
def login_token():
    resp = send_request(
        "POST",
        f"{BASE_URL}/api/v1/login",
        json={"username": USERNAME, "password": PASSWORD},
    )
    return resp.json()["data"]["token"]
```

`testcases/test_profile.py`

```python
from common.request_handler import send_request
from config.settings import BASE_URL


def test_profile(login_token):
    resp = send_request(
        "GET",
        f"{BASE_URL}/api/v1/profile",
        headers={"Authorization": f"Bearer {login_token}"},
    )
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["data"]["username"] == "alice"
```

`pytest.ini`

```ini
[pytest]
testpaths = testcases
python_files = test_*.py
python_functions = test_*
addopts = -v
```

#### 请你对照这套范例回答 3 个问题

1. 如果我要换地址，改哪个文件？
2. 如果我要统一改超时，改哪个文件？
3. 如果我要在多个测试里重复登录，为什么不该把登录代码复制到每个测试函数里？

### 14.8 过关标准

做完这一章，你应该已经不只是会“写测试”，而是开始会“组织测试项目”。

### 14.9 复盘题

1. 我是否还把项目结构理解成“摆文件”？
2. 我现在能不能讲清楚每一层的价值？
3. 我最不熟的是导入方式、请求封装，还是配置分层？

---

## 15. 模块十一：日志、报告、标记

### 15.1 本模块目标

做完这一章，你应该做到：

1. 会生成 HTML 报告
2. 知道报告生成后看什么
3. 知道日志该放哪一层
4. 知道标记要先注册再使用
5. 会用 `pytest -m ...` 筛选测试

### 15.2 热身题

请回答：

1. 报告和日志分别解决什么问题？
2. 为什么日志不建议散在每个测试文件里？
3. `@pytest.mark.smoke` 是 pytest 自带标记还是自定义标记？

### 15.3 主练习一：参数解释题

请解释下面命令每一部分的含义：

```bash
pytest --html=reports/report.html --self-contained-html
```

你需要说清楚：

1. 报告生成到哪里
2. `--self-contained-html` 的作用是什么
3. 为什么有时浏览器打开报告还会有兼容问题

### 15.4 主练习二：日志理解题

请解释下面这段日志配置代码：

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("api_test")
```

你需要说清楚：

1. `format` 里每一段代表什么
2. `logger = logging.getLogger("api_test")` 有什么用
3. 为什么推荐统一导入 `logger`

### 15.5 主练习三：标记顺序题

请把下面 3 步按正确顺序排列：

1. 用 `pytest -m smoke` 运行
2. 在 `pytest.ini` 里注册 `smoke`
3. 在测试上写 `@pytest.mark.smoke`

并说明：

为什么这个顺序更符合教材逻辑？

### 15.6 主练习四：效果题

请解释：

- 报告的价值是什么
- 日志的价值是什么
- 标记的价值是什么

要求你不要只写定义，要写“它到底帮我解决了什么问题”。

### 15.7 实操任务

请你自己完成下面动作：

1. 生成一份 HTML 报告
2. 在公共请求层打印日志
3. 给至少 2 条测试加标记
4. 只运行 `smoke` 测试

#### 输出模板

```text
报告生成命令：
报告文件位置：
日志打印内容至少包括：
我加了哪些标记：
我用什么命令只运行了某一类测试：
```

### 15.8 过关标准

做完这一章，你应该已经具备基础失败定位能力。

### 15.9 复盘题

1. 我过去是不是把报告理解成“只是导出一个页面”？
2. 我现在是否知道日志应该放在哪一层？
3. 我还会不会把“先注册标记”和“先使用标记”的顺序搞反？

---

## 16. 模块十二：完整项目、README、项目表达

### 16.1 本模块目标

做完这一章，你应该做到：

1. 能给自己的项目定范围
2. 知道一个完整小项目至少该有哪些内容
3. 能写最小 README
4. 能用自己的话介绍项目

### 16.2 热身题

请回答：

1. 一个完整接口自动化练习项目至少应该包含什么？
2. README 为什么重要？
3. 为什么项目最终不只是“能跑”，还要“能讲”？

### 16.3 主练习一：项目范围设计

请基于你现在的本地接口服务，列出一套最小项目范围。

要求至少包含：

1. 健康检查
2. 登录
3. 用户资料
4. 商品列表或详情
5. 商品新增删除链路

### 16.4 主练习二：README 结构设计

请写出你准备放进 README 的章节目录。

至少要有：

1. 项目简介
2. 技术栈
3. 项目结构
4. 启动服务方式
5. 执行测试方式
6. 生成报告方式
7. 已覆盖场景

### 16.5 主练习三：项目介绍

请用 5 到 8 句话介绍你的项目。

要求至少包含：

1. 这是个什么项目
2. 用了什么技术栈
3. 测了哪些接口
4. 做了什么分层
5. 解决了什么问题

### 16.6 主练习四：复盘题

请写出：

1. 这套项目里你最满意的地方
2. 这套项目里你最薄弱的地方
3. 如果再给你一天，你会优先补什么

### 16.7 实操任务

请实际完成下面 3 件事：

1. 跑一次完整测试
2. 生成一份最终报告
3. 写一版最小 README

### 16.8 过关标准

做完这一章，你至少应该能做到：

- 项目能运行
- 项目有 README
- 你能把项目讲清楚

### 16.9 复盘题

1. 我现在能不能把项目清楚讲给别人听？
2. 别人拿到我的项目，能不能知道怎么运行？
3. 我最需要补的是代码能力，还是表达能力？

---

## 17. 模块十三：软件测试基础与面试高频

### 17.1 本模块目标

做完这一章，你应该做到：

1. 能回答常见测试理论问题
2. 能说清严重程度和优先级
3. 能解释冒烟测试和回归测试
4. 能说出常见测试设计方法
5. 面试时不只会讲代码

### 17.2 热身题

请回答：

1. 软件测试的目的是什么？
2. 冒烟测试和回归测试有什么区别？
3. 严重程度和优先级的区别是什么？

### 17.3 主练习一：定义题

请分别解释：

1. 黑盒测试
2. 白盒测试
3. 灰盒测试
4. 单元测试
5. 集成测试
6. 系统测试
7. 验收测试

### 17.4 主练习二：缺陷题

请回答：

1. 一个合格缺陷单至少要写哪些内容？
2. 缺陷生命周期常见状态有哪些？
3. 漏测和误报分别是什么？

### 17.5 主练习三：测试设计方法

请解释：

1. 等价类
2. 边界值
3. 场景法
4. 错误推测法

并举一个你自己的接口测试例子。

### 17.6 主练习四：面试题模板

请分别写出你对下面问题的回答：

1. 你怎么理解测试工作？
2. 如果时间不够，你怎么测？
3. 你怎么设计测试用例？
4. 测试什么时候介入最好？

### 17.7 实操任务

请把你自己的答案录成 3 分钟以内的一段“口头自述”，或者直接写成一份面试回答稿。

### 17.8 过关标准

做完这一章，你应该已经不只是“会写接口自动化代码”，还开始具备测试岗位基础表达能力。

### 17.9 复盘题

1. 我最怕被问到哪类测试理论问题？
2. 我现在能不能把“严重程度 vs 优先级”讲清楚？
3. 我是更缺测试理论，还是更缺项目表达？

---

## 18. 综合实战作业

### 18.1 作业目标

请把前面所有模块串起来，完成一套“可解释、可演示、可复盘”的最小项目。

### 18.2 作业要求

至少完成下面这些：

1. 有明确项目范围
2. 有基础接口测试
3. 有至少 1 条链路测试
4. 有参数化
5. 有 fixture
6. 有 `config/`、`common/`、`data/`、`testcases/`
7. 有报告
8. 有 README

### 18.3 最终提交物

请你至少准备下面这些材料：

1. 项目目录
2. 测试代码
3. 一份报告
4. 一份 README
5. 一段 1 分钟项目介绍

### 18.4 自评表

请给自己打分，每项 1 到 5 分：

1. 我能解释接口测试基础概念
2. 我能独立发接口请求
3. 我能用 `pytest` 写测试
4. 我能解释参数化和 fixture
5. 我能组织项目结构
6. 我能看懂报告和日志
7. 我能讲清楚这个项目

### 18.5 最终复盘

请写一段 150 到 300 字的复盘，回答：

1. 这套教材和讲义与练习让我真正学会了什么
2. 我最不稳的地方是什么
3. 接下来我准备往哪一块继续深入

---

## 19. 你可以怎么反复用这份讲义与练习

### 第一次使用

按顺序做，不追求一次答得完美。

### 第二次使用

重点补：

- 你答得最含糊的概念题
- 你最容易写错的实操题

### 第三次使用

把后半部分题目当面试模拟题来练。

---

## 20. 最后给你的使用建议

如果你觉得一整份讲义与练习量很大，不用硬着急。

你可以按下面节奏走：

1. 每次只做 1 个模块
2. 每个模块先做热身题
3. 再做 1 到 2 个主练习
4. 最后一定做复盘

这样你会更容易真正吸收，而不是做成“刷题”。
