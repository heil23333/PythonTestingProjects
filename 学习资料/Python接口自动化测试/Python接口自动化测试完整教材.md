# Python接口自动化测试完整教材

## 1. 这本教材的定位

这本教材面向的是这样一类学习者：

- 想系统学习 Python 接口自动化测试
- 不满足于只看知识点提纲
- 希望按一条自然的学习顺序，从基础概念一路走到完整项目

所以这本教材不是：

- 速查表
- 面试题清单
- 零散知识点合集

它更像一本“从浅到深带你往前走”的入门教材。

你可以把它理解成 4 个阶段：

1. 先建立接口测试认知
2. 再学会用 Python 发请求
3. 再学会用 `pytest` 写可执行测试
4. 最后整理成一个小型项目并学会复盘

---

## 2. 学习这门内容时最容易出现的误区

在正式开始前，先说清楚几个常见误区。

### 2.1 误区一：先学很多框架，再理解接口

这是最常见的走偏方式。

很多人一上来就看：

- fixture
- 参数化
- 报告
- 日志
- 项目结构

但这时候他连下面这些基础问题都没有真正搞清楚：

- 接口是什么
- 请求到底发了什么
- 响应到底回了什么
- 状态码和业务码是什么关系

这样后面学得会很虚。

### 2.2 误区二：只会调成功场景

如果你学接口测试时，脑子里只想着：

- 登录成功
- 查询成功
- 新增成功

那你很容易陷入一种假象：

“我已经会接口测试了。”

但真正的接口测试，价值往往更多体现在：

- 参数错误怎么处理
- 用户不存在怎么处理
- 未登录怎么处理
- 资源不存在怎么处理

所以接口测试不是“只会把接口调通”，而是“会系统地验证接口在各种场景下是否符合预期”。

### 2.3 误区三：把脚本当测试

例如下面这段：

```python
resp = requests.get(url)
print(resp.json())
```

这能算代码，但还不能算测试。

因为测试至少应该有：

- 明确预期
- 自动断言
- 可重复执行
- 可组织和可筛选

这也是为什么后面要引入 `pytest`。

---

## 3. 你最终要学会的，不只是“会写代码”

这门内容真正要学会的，不只是几段 Python 代码，而是一整套能力。

你最终至少要具备下面这些能力：

1. 看懂接口文档
2. 能手工调通接口
3. 能把手工操作改成 Python 代码
4. 能用测试思维拆测试点
5. 能用 `pytest` 组织和执行测试
6. 能处理登录、token、接口关联
7. 能整理项目结构
8. 能看报告、看日志、定位失败
9. 能把项目讲清楚

所以你后面每学一章，都最好问自己一句：

“这一章到底在帮我补哪种能力？”

---

## 4. 什么是接口

很多人第一次听“接口”这个词，会觉得它很抽象。

其实你可以先用一个非常直白的方式理解：

**接口就是系统对外提供的一种固定交互入口。**

例如：

- 你给登录地址发用户名密码，它返回登录结果
- 你给商品列表地址发分页参数，它返回商品列表
- 你给商品详情地址发商品 ID，它返回商品详情

这些“能接收请求并返回结果的地址”，本质上就是接口。

### 4.1 为什么接口不是页面

页面更像是给人看的。

接口更像是给程序之间通信用的。

页面通常包含：

- 布局
- 按钮
- 输入框
- 文案

接口通常更关心：

- 请求方法
- 请求地址
- 请求参数
- 返回状态
- 返回数据

所以接口测试和页面测试虽然都属于测试，但关注点完全不一样。

### 4.2 一个简单的接口例子

例如：

```text
POST http://127.0.0.1:5001/api/v1/login
```

这个接口的含义是：

- 你用 `POST` 方法向这个地址发请求
- 请求体里带用户名和密码
- 服务端会返回你登录成功还是失败

你现在可以先把接口理解成：

**一个有规则的“请求入口”。**

---

## 5. 什么是接口测试

接口测试的核心，不是“能请求出去”，而是：

**验证接口的输入、输出、业务规则和异常处理是否符合预期。**

这句话可以拆开来理解。

### 5.1 输入是否正确

例如：

- 参数传全了没有
- 参数格式对不对
- 参数类型对不对
- 参数为空时怎么处理

### 5.2 输出是否正确

例如：

- 状态码是否正确
- 返回体结构是否正确
- 返回的业务码和消息是否正确
- 关键字段值是否正确

### 5.3 业务规则是否正确

例如：

- 未登录是否不能访问资料接口
- 删除后的商品还能不能被查到
- 错误密码是否应该返回登录失败

### 5.4 异常处理是否合理

例如：

- 缺少参数是否提示清楚
- 用户不存在是否返回合理错误
- 资源不存在是否返回正确状态

所以接口测试不是“看看能不能返回东西”，而是：

**要系统验证接口在正常和异常场景下的行为。**

---

## 6. 接口测试和页面测试的区别

这类问题面试也很常问。

你可以从这几个角度理解。

### 6.1 页面测试更贴近用户操作

页面测试通常是：

- 打开页面
- 点击按钮
- 输入文本
- 验证页面展示

它更贴近用户体验。

### 6.2 接口测试更贴近系统交互

接口测试通常是：

- 直接发请求
- 带参数
- 看状态码和返回数据
- 验证业务逻辑

它更贴近后端和服务层行为。

### 6.3 两者关注点不同

页面测试更关注：

- 页面是否可用
- 交互是否正常
- 文案、展示、样式是否正确

接口测试更关注：

- 数据是否正确
- 逻辑是否正确
- 权限是否正确
- 异常是否处理得当

### 6.4 为什么接口测试通常更适合自动化入门

因为接口测试通常：

- 更稳定
- 更快
- 更容易覆盖异常场景
- 不容易受页面变化影响

这就是为什么很多测试学习路径都会先从接口自动化开始。

---

## 7. HTTP 是什么

如果你要学接口自动化，HTTP 是一定绕不过去的。

你可以先把 HTTP 理解成：

**客户端和服务端约定好的通信规则。**

当你写：

```python
requests.get(...)
```

本质上你就是在发送一个 HTTP 请求。

当服务端给你返回：

- 状态码
- 响应头
- 响应体

本质上它就是在回一个 HTTP 响应。

### 7.1 为什么 HTTP 很重要

因为后面你学的大多数东西，其实都建立在 HTTP 之上。

例如：

- `GET` / `POST`
- 请求头
- 查询参数
- 请求体
- 状态码
- 响应 JSON

如果你不理解 HTTP，就会出现一种情况：

- 代码会写一点
- 但请求发错了也不知道为什么

所以接口自动化里，HTTP 不是“额外知识”，而是底层基础。

---

## 8. 一个请求通常由什么组成

一个请求通常至少包含这几部分：

1. URL
2. 请求方法
3. 请求头
4. 查询参数
5. 请求体

我们一项一项看。

### 8.1 URL

例如：

```text
http://127.0.0.1:5001/api/v1/login
```

它告诉你：

- 请求发到哪里

你做接口测试时，一定要先看清楚：

- 地址有没有写错
- 路径有没有写错

因为很多“看起来像业务问题”的报错，最后其实只是 URL 不对。

### 8.2 请求方法

最常见的有：

- `GET`
- `POST`
- `PUT`
- `PATCH`
- `DELETE`

你现在先把它们理解成：

- `GET`：查
- `POST`：提交、新增、登录
- `PUT/PATCH`：修改
- `DELETE`：删除

但要注意：

它们是“通常这样用”，不是绝对铁律。

例如有些接口设计得不规范，也可能出现看起来不太合理的方法使用。

### 8.3 请求头 `headers`

请求头最常见的两个作用是：

1. 告诉服务端请求体是什么格式
2. 携带鉴权信息

例如：

```python
headers = {"Content-Type": "application/json"}
```

表示：

- 我发的是 JSON

再例如：

```python
headers = {"Authorization": f"Bearer {token}"}
```

表示：

- 我带了 token

### 8.4 查询参数 `params`

查询参数通常是附加在 URL 后面的。

例如：

```python
params = {"page": 1, "page_size": 10}
```

这种通常用于：

- 列表分页
- 搜索条件
- 查询过滤

### 8.5 请求体

请求体常见有两种：

- JSON 请求体
- 表单请求体

这也是后面 `json=` 和 `data=` 区别的基础。

---

## 9. 一个响应通常由什么组成

响应通常由下面这些组成：

1. 状态码
2. 响应头
3. 响应体

### 9.1 状态码

状态码先告诉你，这次 HTTP 层面大概发生了什么。

例如：

- `200`：成功
- `201`：创建成功
- `400`：请求参数有问题
- `401`：认证失败
- `403`：无权限
- `404`：资源不存在
- `500`：服务端异常

### 9.2 响应体

现代接口最常见的是返回 JSON。

例如：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "status": "ok"
  }
}
```

你做测试时要学会看：

- `code`
- `message`
- `data`

因为很多时候，真正的业务结果都藏在这些字段里。

---

## 10. 状态码和业务码为什么不能混

这是接口测试里的核心认知之一。

### 10.1 HTTP 状态码解决的是通信层结果

例如：

- 请求成功没有
- 请求格式对不对
- 有没有权限
- 资源是否存在

### 10.2 业务码解决的是业务层结果

例如：

- 登录成功
- 用户不存在
- 密码错误
- 商品不存在

你要记住：

**HTTP 成功，不等于业务一定成功。**

例如：

```python
assert resp.status_code == 200
```

这只能说明 HTTP 层成功了。

但你还需要继续断言：

```python
body = resp.json()
assert body["code"] == 0
assert body["message"] == "success"
```

### 10.3 为什么很多初学者会在这里出错

因为初学者特别容易只盯着状态码。

但接口测试里真正成熟的断言通常是：

1. 先断 HTTP 状态码
2. 再断业务码
3. 再断关键字段

如果你只断第一层，很多错误会漏掉。

---

## 11. `params`、`json`、`data` 到底怎么区分

这是最常见的基础卡点之一。

先记一句非常重要的话：

- `params`：拼在 URL 后面
- `json`：按 JSON 请求体发送
- `data`：按表单或普通请求体发送

### 11.1 `params`

例如：

```python
requests.get(url, params={"page": 1, "page_size": 10})
```

它通常会变成类似：

```text
...?page=1&page_size=10
```

所以它特别适合：

- 列表分页
- 条件查询
- 搜索接口

### 11.2 `json`

例如：

```python
requests.post(url, json={"username": "alice", "password": "123456"})
```

这表示：

- 请求体按 JSON 发出去

`requests` 还会帮你自动补：

```text
Content-Type: application/json
```

这就是为什么登录、新增、修改这类接口，很多时候优先想到 `json=`。

### 11.3 `data`

例如：

```python
requests.post(url, data={"name": "alice", "city": "shanghai"})
```

这更像是表单风格请求。

所以你不应该靠“是不是字典”来判断，而应该看：

**服务端到底希望你按什么格式发。**

### 11.4 一个最容易踩的坑

如果服务端代码在按 JSON 取数据：

```python
request.get_json()
```

那你却用：

```python
data={...}
```

就很可能取不到。

所以：

- 看文档
- 看服务端预期

比死记语法更重要。

---

## 12. `resp.text` 和 `resp.json()` 的区别

这部分一定要理解，不然后面排错会很痛苦。

### 12.1 `resp.text`

拿到的是原始响应文本。

它通常是字符串。

适合用来：

- 先整体看返回内容
- 排查响应是不是合法 JSON
- 看报错页面原文

### 12.2 `resp.json()`

把响应按 JSON 解析成 Python 对象。

如果返回的是 JSON 对象，通常变成字典。

如果返回的是 JSON 数组，通常变成列表。

适合用来：

- 取字段
- 写断言
- 做后续逻辑处理

### 12.3 一个非常重要的认知

`resp.json()` 会不会报错，和“状态码是不是 200”没有直接关系。

它真正取决于：

**整个响应体是不是合法 JSON。**

例如：

```json
{"code":10013,"message":"user not found","data":null}
```

虽然这可能对应一个 `404`，但它依然是 JSON，所以可以正常 `resp.json()`。

### 12.4 什么情况下 `resp.json()` 容易报错

例如：

- 返回 HTML 错误页
- 返回空响应
- 返回根本不是 JSON 的纯文本

所以排错时，经常先看：

```python
print(resp.status_code)
print(resp.text)
```

确认内容正常后，再去 `resp.json()`。

---

## 13. JSON 里的 `null` 和“不是 JSON”是两回事

这也是一个初学者特别容易混掉的点。

例如下面这个响应：

```json
{
  "code": 10013,
  "message": "user not found",
  "data": null
}
```

这里的 `data` 虽然是 `null`，但整个响应依然是合法 JSON。

所以在 Python 里：

```python
body = resp.json()
```

是可以正常执行的。

然后：

```python
body["data"] is None
```

也会成立。

你一定要把下面两件事分开：

1. JSON 里的某个字段值是 `null`
2. 整个响应体根本不是 JSON

这两件事完全不是一回事。

---

## 14. Cookie、Session、Token、JWT 怎么理解

接口自动化里，这几个词出现频率很高。

你现在不用追求非常底层，只要先建立够用认知就行。

### 14.1 Cookie

服务端给客户端的一小段信息，客户端后续请求时可以再带回来。

### 14.2 Session

服务端保存的一段会话状态。

### 14.3 Token

客户端拿到后，可在后续请求中带上的身份凭证。

### 14.4 JWT

一种常见的 token 形式。

### 14.5 当前阶段你最该掌握的是什么

你当前最常见的场景是：

1. 登录拿 token
2. 后续请求带 token

所以最重要的是理解：

- 为什么要先登录
- token 通常怎么放进请求头

而不是一开始就死磕 JWT 的内部结构。

---

## 15. 如何读一份接口文档

读接口文档时，不要只看接口地址。

你至少要看下面这些：

1. 请求方法
2. 接口地址
3. 是否需要登录
4. 请求参数
5. 请求头要求
6. 请求体示例
7. 成功响应示例
8. 失败响应示例

### 15.1 读完一份接口文档后，你应该能回答什么

至少应该能回答：

1. 这个接口怎么调
2. 它需要什么参数
3. 它是否需要鉴权
4. 成功时会返回什么
5. 失败时会返回什么

如果你读完文档后还答不出这些问题，说明你其实还没真正看懂。

---

## 16. 如何手工调一个接口

在真正写 Python 之前，先能手工调通接口非常重要。

常见工具有：

- Postman
- Apifox

### 16.1 为什么这一步不能跳

因为它能帮你先把问题分层。

如果手工都调不通，通常说明问题可能在：

- 地址不对
- 方法不对
- 参数不对
- token 不对
- 接口本身有问题

而不是代码写法问题。

### 16.2 手工调接口时你应该记录什么

至少记录：

1. URL
2. 请求方法
3. 请求头
4. 请求参数
5. 成功响应
6. 失败响应

这会直接帮助你后面写自动化测试。

---

## 17. 接口测试到底测什么

这是测试思维真正开始进入的时候。

一个接口至少可以从下面这些方向去设计测试：

1. 功能正确性
2. 参数校验
3. 边界值
4. 权限和鉴权
5. 资源是否存在
6. 业务规则
7. 异常场景

### 17.1 以登录接口为例

至少可以想到：

- 正确用户名密码登录成功
- 密码错误
- 用户名为空
- 密码为空
- 用户不存在
- 未按要求传参

### 17.2 以商品详情接口为例

至少可以想到：

- 商品存在
- 商品不存在
- 非法 ID
- 未登录是否能访问

所以测试点不是“随便想两个”，而是要形成结构化思考。

---

## 18. 为什么 Python 基础不需要先学得特别重

你现在是做接口自动化，不是转做算法工程。

所以初期真正高频用到的 Python 基础非常集中：

1. 变量
2. 字符串
3. 列表
4. 字典
5. `if`
6. `for`
7. 函数
8. 导入
9. JSON 读写

这意味着：

你不用因为“Python 还没完全学完”就不敢开始接口自动化。

你是可以边做接口自动化，边把够用的 Python 补起来的。

---

## 19. 接口自动化里最重要的数据结构：字典

你后面会发现，字典出现频率非常高。

例如：

- 请求头是字典
- 请求体很多时候是字典
- 响应 JSON 通常会变成字典

例如：

```python
headers = {"Authorization": f"Bearer {token}"}
payload = {"username": "alice", "password": "123456"}
body = resp.json()
```

所以：

**如果你对字典不熟，接口自动化会很吃力。**

你至少要会：

```python
body["code"]
body["message"]
body["data"]["user"]["username"]
```

---

## 20. `f-string` 为什么在接口自动化里特别常见

例如：

```python
token = "token-1"
product_id = 7
```

你很常会写：

```python
headers = {"Authorization": f"Bearer {token}"}
url = f"http://127.0.0.1:5001/api/v1/products/{product_id}"
```

这里的核心作用就是：

**把变量值直接插进字符串里。**

这比字符串拼接更直观。

所以你后面看到：

```python
f"...{变量}..."
```

不要慌，它只是“变量插值”的一种更好用写法。

---

## 21. `json` 模块为什么一定会用到

接口自动化里，JSON 几乎到处都是。

你会碰到：

- 响应 JSON
- 测试数据文件
- 环境配置文件

所以这些函数会经常出现：

- `json.loads()`
- `json.dumps()`
- `json.load()`
- `json.dump()`

### 21.1 先记住最实用的区分

- `load / dump`：处理文件
- `loads / dumps`：处理字符串

这是当前阶段最值得先记住的一点。

---

## 22. 用 `requests` 开始真正发请求

当你已经理解了接口、HTTP、请求和响应之后，就可以进入代码阶段了。

最常用的库就是：

- `requests`

### 22.0 先把 `requests` 的角色想清楚

`requests` 不是测试框架，它只是一个“帮你发 HTTP 请求”的 Python 库。

它负责的事情主要有：

1. 帮你发 GET、POST、PUT、DELETE 等请求
2. 帮你把请求头、请求参数、请求体带出去
3. 帮你拿回响应对象
4. 让你可以继续看状态码、响应文本、JSON 数据

你可以先把它理解成：

**把你在 Postman、Apifox 里手工点的动作，翻译成 Python 代码。**

所以学习 `requests` 的正确顺序应该是：

1. 先知道自己要发什么请求
2. 再知道这个请求在 `requests` 里怎么写
3. 最后再处理响应

如果一上来只记语法，不知道它对应的是哪种 HTTP 行为，就会学得很虚。

### 22.0.1 安装和验证

如果你的环境里还没有装 `requests`，可以先执行：

```bash
pip install requests
```

如果你在虚拟环境里学习，更推荐先激活虚拟环境，再安装：

```bash
source .venv/bin/activate
pip install requests
```

安装后可以简单验证：

```bash
python -c "import requests; print(requests.__version__)"
```

只要能正常输出版本号，就说明库已经可用。

### 22.0.2 `requests` 最常见的返回对象是什么

你每次写：

```python
resp = requests.get(...)
```

这里的 `resp` 本质上是一个响应对象。你后面最常用的就是它的这几个成员：

- `resp.status_code`
- `resp.text`
- `resp.json()`
- `resp.headers`

它们分别回答的是：

1. 这次请求在 HTTP 层是成功还是失败
2. 原始响应文本是什么
3. 如果响应是 JSON，解析后长什么样
4. 响应头里带了什么信息

所以很多初学者的调试顺序可以先固定成：

```python
print(resp.status_code)
print(resp.text)
```

先确认接口到底回了什么，再决定要不要继续 `resp.json()`。

### 22.1 你当前最常见的写法

```python
requests.get(...)
requests.post(...)
requests.delete(...)
```

这 3 个已经能覆盖你当前阶段大多数练习场景了。

你可以先这样理解：

- `requests.get()`：拿数据
- `requests.post()`：提交数据
- `requests.delete()`：删除数据

当然这不是绝对规则，但在你当前学习接口自动化的阶段，这样记是够用的。

### 22.1.1 一个请求通常由哪几部分组成

把 `requests` 写法和 HTTP 请求对起来看，会更容易理解。

例如下面这段：

```python
resp = requests.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
    headers={"X-Test": "demo"},
    timeout=5,
)
```

它至少包含这些部分：

1. 请求方法：`POST`
2. 请求地址：`http://127.0.0.1:5001/api/v1/login`
3. 请求体：`json={...}`
4. 请求头：`headers={...}`
5. 超时控制：`timeout=5`

所以你以后看 `requests` 代码时，不要只看“这一行像不像对”，而要按这几个维度拆开看。

### 22.2 一个最小 GET 请求例子

```python
import requests

resp = requests.get("http://127.0.0.1:5001/health")
print(resp.status_code)
print(resp.json())
```

这段代码的阅读顺序应该是：

1. 我在发一个 GET 请求
2. 请求地址是 `/health`
3. 返回结果先看状态码
4. 如果返回体是 JSON，再继续 `resp.json()`

### 22.2.1 如果我要带查询参数怎么办

这时候就要用 `params=`

```python
resp = requests.get(
    "http://127.0.0.1:5001/api/v1/products",
    params={"page": 1, "page_size": 5},
)
```

这里的含义是：

- 不把参数放进请求体
- 而是把参数拼到 URL 后面

实际请求地址会接近：

```text
http://127.0.0.1:5001/api/v1/products?page=1&page_size=5
```

所以你要建立一个稳定判断：

- URL 后面的查询参数：优先想到 `params`
- 请求体里的 JSON：优先想到 `json`
- 表单体：优先想到 `data`

### 22.3 一个最小 POST 请求例子

```python
resp = requests.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
)
```

你现在真正要建立的是：

- 我能手工调
- 我也能用 Python 调

这两者之间要自然打通。

### 22.3.1 为什么登录更常用 `json=`

因为现在很多接口文档里的登录请求体，长这样：

```json
{
  "username": "alice",
  "password": "123456"
}
```

这就是标准 JSON 请求体。

所以在 `requests` 里通常写：

```python
resp = requests.post(
    "http://127.0.0.1:5001/api/v1/login",
    json={"username": "alice", "password": "123456"},
)
```

这里的 `json=` 会帮你做两件事：

1. 把 Python 字典转成 JSON 字符串
2. 自动补 `Content-Type: application/json`

这也是为什么当前阶段很多接口优先教你用 `json=`。

### 22.3.2 `json=`、`data=`、`params=` 到底怎么选

这三个非常高频，一定要讲清楚。

#### `params=`

用于 URL 查询参数：

```python
requests.get(url, params={"page": 1})
```

#### `json=`

用于 JSON 请求体：

```python
requests.post(url, json={"username": "alice"})
```

#### `data=`

用于表单请求体：

```python
requests.post(url, data={"name": "alice"})
```

你现在最实用的记忆方法就是：

1. 查询条件放 URL 后面：`params`
2. 登录、新增、修改常见 JSON 体：`json`
3. 老接口或表单接口：`data`

### 22.3.3 一个带请求头的完整例子

等你拿到 token 之后，请求通常会升级成这样：

```python
token = "token-1"

resp = requests.get(
    "http://127.0.0.1:5001/api/v1/profile",
    headers={"Authorization": f"Bearer {token}"},
)
```

这里你要重点看懂两件事：

1. `headers=` 是在带请求头
2. `f"Bearer {token}"` 是把 token 动态拼进字符串

这就是接口关联在代码里的基本落地方式。

### 22.3.4 一个当前阶段够用的 `requests` 范例

下面这段代码，基本已经把你当前阶段最常见的写法串起来了：

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

这段范例的学习价值不在“代码长不长”，而在于它体现了完整顺序：

1. 先登录
2. 再提取 token
3. 再把 token 用到下一条请求

当你能把这段完全看懂时，`requests` 这一章才算真正入门。

### 22.4 学 `requests` 时最容易犯的错

这里顺手把几个高频坑直接列出来：

1. 把 `json=` 和 `data=` 混掉
2. 一上来就直接 `resp.json()`，没先看 `status_code` 和 `text`
3. 把 URL 写错导致返回 HTML，却以为是接口逻辑错了
4. 没带 token，却以为是接口坏了
5. 每次排查都只看断言失败，不看原始响应

你越早养成“先看状态码，再看响应体”的习惯，后面学 `pytest` 会越稳。

---

## 23. 为什么刚开始不建议立刻过度封装

很多初学者一学会 `requests`，就想马上写：

- 通用框架
- 基类
- 多层封装
- 很多工具方法

这通常会让你过早陷入复杂度里。

当前阶段更合理的目标应该是：

1. 先把基础请求写明白
2. 先搞清 `params/json/data`
3. 先看懂响应
4. 先能写清楚断言

之后再谈收敛和封装，顺序会更自然。

---

## 24. 从“请求脚本”到“测试用例”的关键一步

例如下面这段：

```python
resp = requests.get(url)
print(resp.status_code)
print(resp.json())
```

它还只是脚本。

真正往测试走时，核心变化是：

```python
assert resp.status_code == 200
assert body["code"] == 0
```

所以测试和脚本的关键区别是：

- 有没有明确预期
- 有没有自动断言

而 `pytest` 则是在这个基础上，继续帮你把测试组织起来。

---

## 25. `pytest` 为什么重要

`pytest` 不是“多一个命令而已”，它是从零散脚本升级到系统化测试的关键。

它能帮你：

1. 自动发现测试
2. 执行断言
3. 展示失败位置
4. 支持参数化
5. 支持 fixture
6. 支持插件和配置

所以：

- `requests` 负责发请求
- `pytest` 负责组织和运行测试

这两个角色一定要分清。

### 25.1 安装 `pytest` 和验证安装成功

如果你的环境里还没有 `pytest`，先安装：

```bash
pip install pytest
```

如果你在虚拟环境里学习，建议这样做：

```bash
source .venv/bin/activate
pip install pytest
```

安装完后，先不要急着写复杂代码，先验证：

```bash
pytest --version
```

只要能正常输出版本号，就说明 `pytest` 已经可用了。

### 25.2 一个最小 `pytest` 测试长什么样

下面是一条最小但完整的测试：

```python
import requests


def test_health():
    resp = requests.get("http://127.0.0.1:5001/health")
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
```

这里你要认识 4 个最基础的点：

1. 测试函数通常以 `test_` 开头
2. `pytest` 会自动发现这种测试函数
3. `assert` 是最基础的断言方式
4. 失败时 `pytest` 会告诉你断言停在哪一行

### 25.3 为什么这条代码已经不只是脚本

因为它已经具备测试最关键的 3 个特点：

1. 有明确预期
2. 有自动断言
3. 可以反复运行

对比一下：

#### 只是脚本

```python
resp = requests.get(url)
print(resp.json())
```

#### 真正的测试

```python
def test_health():
    resp = requests.get(url)
    assert resp.status_code == 200
```

这一步认知非常重要。很多人明明已经开始学自动化，却还在用“写脚本”的方式思考问题。

### 25.4 `pytest` 最常用的几条命令到底怎么理解

先看这几条最常用命令：

```bash
pytest
pytest -v
pytest -s -v
pytest -k login
```

你现在可以这样理解：

#### `pytest`

执行默认发现到的全部测试。

#### `pytest -v`

`-v` 表示显示更详细的测试名称和结果。

#### `pytest -s -v`

`-s` 表示不要屏蔽 `print()` 输出，方便调试。

#### `pytest -k login`

只执行名称匹配 `login` 的测试。

你当前阶段最实用的其实就是：

```bash
pytest -s -v
```

因为你正在学习阶段，最需要的是：

1. 看到详细执行结果
2. 看到你自己打印的调试信息

### 25.5 `pytest` 是怎么发现测试的

这也是很多初学者会迷糊的一点。

默认情况下，它通常会识别：

1. 文件名以 `test_` 开头或以 `_test` 结尾
2. 函数名以 `test_` 开头
3. 类名以 `Test` 开头

所以你现在写：

```python
def test_login():
    ...
```

它能被收集。

但如果你写：

```python
def login():
    ...
```

那它通常不会被当成测试函数。

这也解释了为什么：

- fixture 可以注入到测试函数
- 却不能自动注入到普通辅助函数

因为 `pytest` 根本不会把普通函数当成它要管理的测试对象。

### 25.6 一个完整的 `pytest + requests` 范例

下面这段代码很适合当你当前阶段的范例模板：

```python
import requests


BASE_URL = "http://127.0.0.1:5001"


def test_login_success():
    resp = requests.post(
        f"{BASE_URL}/api/v1/login",
        json={"username": "alice", "password": "123456"},
        timeout=5,
    )
    body = resp.json()

    assert resp.status_code == 200
    assert body["code"] == 0
    assert body["message"] == "success"
    assert "token" in body["data"]
```

这段范例至少体现了：

1. `requests` 用来发请求
2. `pytest` 用测试函数和 `assert` 组织测试
3. 断言不只看状态码，还看业务码和关键字段

如果你只会写请求，不会把它写成上面这种结构，那就说明你还停留在脚本阶段。

---

## 26. 参数化为什么是接口测试的高频能力

因为同一个接口通常不是只测一条数据。

例如登录接口很明显就要测多组数据：

- 成功
- 密码错误
- 用户名为空
- 用户不存在

如果每一条都单独写测试，会很重复。

这时候参数化就出现了。

它的本质是：

**同一套测试逻辑，重复跑多组数据。**

所以你后面看到：

```python
@pytest.mark.parametrize(...)
```

不要先把它当“难语法”，先把它理解成：

“多组数据重复执行同一个测试。”

---

## 27. fixture 为什么也是高频能力

因为很多测试前面都要做重复准备动作。

例如：

- 测资料接口前要先登录
- 测商品删除前要先创建商品
- 测链路时要先 reset 数据

如果每个测试都自己写一遍这些前置动作，会很乱。

fixture 的价值就在于：

**把前置步骤和测试逻辑分开。**

所以：

- 参数化解决“多组数据”
- fixture 解决“重复前置”

这两者经常一起出现。

---

## 28. `conftest.py` 为什么特别重要

当 fixture 变多后，如果你还都写在测试文件里，会很快乱。

`conftest.py` 的价值就是：

把公共 fixture 集中放在一个地方，并让 `pytest` 自动发现。

它最容易误解的点是：

你不会手动导入它。

你是直接这样用：

```python
def test_profile(login_token):
    ...
```

这就是为什么很多初学者第一次接触时会觉得它“有点玄”。

但本质上它只是：

**把公共前置能力集中管理。**

---

## 29. 为什么项目结构必须开始整理

当前面这些能力逐渐叠加后，代码量自然会变多。

这时如果你还保持：

- 一个文件里全写
- 每个文件都重复 URL
- 每个文件都重复请求和断言

项目就会迅速失控。

所以到这个阶段，整理结构不是“高级玩法”，而是必须动作。

---

## 30. 项目结构的核心不是“目录长什么样”，而是“职责怎么分”

这是非常重要的一点。

例如：

- `config/` 负责环境和常量
- `common/` 负责公共请求、日志、断言
- `data/` 负责测试数据
- `testcases/` 负责业务测试

真正重要的不是“名字好不好看”，而是：

以后改配置、改数据、改请求逻辑、改测试逻辑时，改动范围会不会变小。

这才是项目结构的实际价值。

### 30.1 一个当前阶段够用的项目结构范例

你现在不需要一上来就搞特别复杂的框架，但至少应该理解下面这套结构：

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

请你一定注意：

这不是“为了看起来像项目”才这样放，而是因为每一层都在解决具体问题。

### 30.2 每一层到底解决什么问题

#### `config/settings.py`

放配置，例如：

- `BASE_URL`
- `TIMEOUT`
- 默认账号密码

这样做的效果是：

- 地址和超时不需要每个测试文件重复写
- 换环境时改动范围更小

#### `common/request_handler.py`

放统一请求入口。

这样做的效果是：

- 默认超时统一
- 日志统一
- 以后想加重试、公共请求处理时改动集中

#### `common/assert_util.py`

放通用断言。

这样做的效果是：

- 重复成功断言可以少写很多次
- 测试文件更聚焦业务逻辑

#### `common/logger.py`

放日志初始化。

这样做的效果是：

- 整个项目日志格式统一
- 排查问题时输出风格一致

#### `data/`

放参数化数据。

这样做的效果是：

- 数据和逻辑分开
- 改测试数据时不容易误改测试逻辑

#### `testcases/`

放真正的业务测试文件。

这样做的效果是：

- 测试入口清楚
- 按业务场景拆文件更自然

#### `conftest.py`

放公共 fixture。

这样做的效果是：

- 登录 token、公共请求头、数据 reset 可以复用
- 测试文件更短

#### `pytest.ini`

放 `pytest` 配置。

这样做的效果是：

- 测试目录、命名规则、默认参数、标记注册统一管理

### 30.3 这个结构放好以后，到底怎么用

这一步你前面一直追问得很对，教材必须讲。

下面我们直接看“放完以后怎么用”。

#### 第一步：配置先落地

`config/settings.py`

```python
BASE_URL = "http://127.0.0.1:5001"
TIMEOUT = 5
USERNAME = "alice"
PASSWORD = "123456"
```

这时别的文件就可以这样导入：

```python
from config.settings import BASE_URL, TIMEOUT
```

#### 第二步：统一请求入口

`common/request_handler.py`

```python
import requests

from config.settings import TIMEOUT


def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    return requests.request(method=method, url=url, **kwargs)
```

这时测试文件就不需要每次都直接写 `requests.get/post/delete` 了，而是可以统一走：

```python
from common.request_handler import send_request
```

然后这样用：

```python
resp = send_request("GET", f"{BASE_URL}/health")
```

或者：

```python
resp = send_request(
    "POST",
    f"{BASE_URL}/api/v1/login",
    json={"username": "alice", "password": "123456"},
)
```

#### 第三步：公共 fixture 放到 `conftest.py`

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

这时测试文件里就可以直接写：

```python
def test_profile(login_token):
    ...
```

你不需要手动导入 `conftest.py`，`pytest` 会自动发现它。

### 30.4 一个“放好以后能直接运行”的完整范例

下面给你一套最小但完整的示例，帮助你把结构和用法真正连起来。

#### `config/settings.py`

```python
BASE_URL = "http://127.0.0.1:5001"
TIMEOUT = 5
USERNAME = "alice"
PASSWORD = "123456"
```

#### `common/request_handler.py`

```python
import requests

from config.settings import TIMEOUT


def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    return requests.request(method=method, url=url, **kwargs)
```

#### `conftest.py`

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

#### `testcases/test_profile.py`

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

#### `pytest.ini`

```ini
[pytest]
testpaths = testcases
python_files = test_*.py
python_functions = test_*
addopts = -v
```

这套范例已经能体现出项目结构真正的价值：

1. 配置集中
2. 请求入口统一
3. 登录前置可复用
4. 测试文件只关注业务断言

---

## 31. 为什么配置应该先收敛

例如下面这些：

- `BASE_URL`
- 用户名密码
- 超时

它们本质上都是“环境信息”，不是“测试逻辑”。

所以更合理的做法是：

先把它们放进配置层。

这样后面：

- 请求入口可以依赖超时
- fixture 可以依赖账号密码
- 测试文件可以依赖 `BASE_URL`

这也是为什么真正的教材顺序应该是：

1. 先讲配置
2. 再讲公共请求入口
3. 再讲其他公共层

而不是把这些知识点平铺。

---

## 32. `send_request()` 到底解决了什么问题

最小版本通常像这样：

```python
def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    return requests.request(method=method, url=url, **kwargs)
```

它不是为了“看起来高级”，而是为了统一入口。

它解决的问题有：

1. 默认超时不需要每个文件都写
2. 后面要加日志时只改一个地方
3. 请求入口统一后，测试文件更聚焦业务场景

所以你要把它理解成：

**从 Day 2 的直接写请求，升级到 Day 5 的统一请求入口。**

---

## 33. 公共断言为什么要开始出现

因为很多成功场景的断言是重复的。

例如：

```python
assert resp.status_code == 200
assert body["code"] == 0
assert body["message"] == "success"
```

如果每个测试都写一遍，后面会越来越烦。

所以才会有：

```python
assert_success_response(resp, body)
```

但你一定要记住：

**通用成功断言可以抽，业务特有断言不要强行抽。**

例如：

```python
assert body["data"]["name"] == "Desk Lamp"
```

这种业务字段断言，还是应该留在测试文件里。

---

## 34. 测试数据为什么要和测试逻辑分开

这是项目化思维里非常关键的一步。

如果你把数据和测试逻辑混在一起，会出现：

- 测试文件太长
- 改数据容易碰到逻辑
- 参数化数据不好维护

所以更推荐：

- 测试逻辑放测试文件
- 测试数据放 JSON 文件

这也是“可维护性”开始进入项目的标志。

---

## 35. 报告和日志为什么放在后面学

因为它们的价值建立在前面已经有测试的前提上。

如果你还没真正会写测试，就先学报告和日志，会很容易本末倒置。

正确顺序应该是：

1. 先会发请求
2. 先会写断言
3. 先会组织测试
4. 再看怎么更好地定位失败

### 35.1 报告的价值

告诉你：

- 哪些测试通过
- 哪些失败
- 失败停在哪

### 35.2 日志的价值

告诉你：

- 发了什么请求
- 传了什么参数
- 回了什么结果

所以：

- 报告更像结果总览
- 日志更像过程记录

---

## 36. 标记为什么也应该在后面学

因为标记本质上是“测试筛选能力”，不是“最前置能力”。

只有当你已经有了一批测试时，标记才真正有价值。

例如：

- 想先只跑核心流程
- 想只跑回归测试

这时才会引入：

- `smoke`
- `regression`

而且这里还有一个教材顺序必须注意的点：

1. 先在 `pytest.ini` 注册标记
2. 再在测试函数上使用标记
3. 最后再讲 `pytest -m ...`

这就是“教材必须循序渐进”的一个典型体现。

---

## 37. 为什么最终还要写 README

因为一个项目最终不是只给你自己看的。

如果没有 README，别人拿到项目后很容易不知道：

- 这是什么
- 怎么启动
- 怎么运行
- 测了什么

所以 README 不是装饰品，而是项目说明书。

一个初学者项目如果有：

- 测试代码
- 报告
- README

它整体就更像一个成品，而不是练习碎片。

---

## 38. 最后一步为什么是“会讲项目”

因为如果你只会写，但讲不清楚，说明你还没有完全内化这套东西。

你最终应该能讲清楚：

1. 测了哪些接口
2. 为什么这样组织目录
3. 登录和 token 怎么关联
4. 正向反向怎么覆盖
5. 报告和日志怎么帮助定位问题

当你能把这些说清楚时，你对这套项目的理解才算比较完整。

---

## 39. 学完之后，你应该怎么判断自己是不是真的学会了

你可以用下面这些问题自查：

1. 我能解释接口测试测什么吗？
2. 我能区分状态码和业务码吗？
3. 我能分清 `params/json/data` 吗？
4. 我能看懂基础 Python 接口测试代码吗？
5. 我能用 `requests` 发请求吗？
6. 我能用 `pytest` 写基础测试吗？
7. 我能解释参数化和 fixture 吗？
8. 我能解释为什么要做项目分层吗？
9. 我能看懂报告和日志吗？
10. 我能把自己的项目讲清楚吗？

如果大多数问题你都能稳定回答，说明你已经不只是“看过”，而是真的学进去了。

---

## 40. 这本教材最希望你带走的一条主线

如果后面你忘了很多细节，也没关系，只要你还记得这条主线，就不容易学乱：

1. 先理解接口和 HTTP
2. 再学会手工调接口
3. 再用 `requests` 发请求
4. 再用 `pytest` 写测试
5. 再学参数化、fixture、接口关联
6. 再整理项目结构
7. 再加报告、日志、标记
8. 最后把它收成一个能讲得清楚的小项目

这就是接口自动化测试对初学者来说最自然、最稳的一条路。
