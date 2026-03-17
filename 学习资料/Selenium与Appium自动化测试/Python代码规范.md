# Python 代码规范

这份规范面向你现在的学习和实战场景：

- Python 基础代码
- Selenium / Appium 自动化测试
- `pytest` 项目
- 页面对象模型 `POM`

目标不是把代码写得“很花”，而是写得：

- 稳
- 清楚
- 方便自己和别人维护

---

## 1. 先记住这 10 条

1. 变量、函数、方法名用 `snake_case`
2. 类名用 `PascalCase`
3. 常量用全大写，如 `BASE_URL`
4. 一个函数只做一件事
5. 公共逻辑不要复制，提取成函数或页面对象
6. 页面对象负责动作和读取，测试负责断言
7. 等待写在该写的位置，不要到处乱加 `sleep()`
8. 不要写含糊命名，如 `data`、`info`、`temp`
9. 导入只保留当前文件真正会用到的东西
10. 先追求可读，再追求“高级”

---

## 2. 命名规范

### 2.1 变量名

用有意义的英文单词，不要只求短。

推荐：

```python
username = "tester"
password = "Selenium123"
login_feedback = "登录失败"
```

不推荐：

```python
u = "tester"
p = "Selenium123"
msg = "登录失败"
```

如果变量表示布尔值，尽量让名字能看出真假含义。

推荐：

```python
is_success = True
is_visible = False
has_error = True
```

### 2.2 函数名和方法名

统一用 `snake_case`。

推荐：

```python
def save_failure_screenshot(driver, name):
    ...

def feedback_text(self):
    ...
```

不推荐：

```python
def SaveFailureScreenshot(...):
    ...

def feedbackText(...):
    ...
```

### 2.3 类名

类名用 `PascalCase`。

推荐：

```python
class LoginPage:
    ...

class DashboardPage:
    ...
```

### 2.4 常量名

不会轻易变化的配置值用全大写。

```python
BASE_URL = "http://127.0.0.1:8000"
USERNAME = "tester"
PASSWORD = "Selenium123"
```

---

## 3. 文件和目录命名

### 3.1 Python 文件名

文件名统一用小写加下划线。

推荐：

```text
login_page.py
dashboard_page.py
test_login.py
tools.py
setting.py
```

### 3.2 测试文件名

pytest 测试文件建议以 `test_` 开头。

```text
test_login.py
test_dashboard.py
```

### 3.3 目录建议

自动化测试项目常见结构：

```text
project/
  conftest.py
  pytest.ini
  config/
  common/
  pages/
  tests/
  artifacts/
```

---

## 4. 导入规范

### 4.1 只导入当前文件真的会用到的东西

如果这个文件里只用了 `By` 和 `Select`，那就只导这两个。

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
```

不要提前把一堆你“可能以后会用”的东西都导进来。

不推荐：

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
```

如果当前文件没用这些，就不要导。

### 4.2 导入顺序

推荐顺序：

1. 标准库
2. 第三方库
3. 自己项目里的模块

例如：

```python
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from config.setting import BASE_URL
```

### 4.3 不要写星号导入

不推荐：

```python
from common.tools import *
```

推荐：

```python
from common.tools import save_failure_screenshot
```

---

## 5. 函数规范

### 5.1 一个函数只做一件事

推荐：

```python
def save_failure_screenshot(driver, name):
    ...
```

不推荐一个函数同时：

- 打开页面
- 登录
- 截图
- 断言
- 写日志

### 5.2 参数名要清楚

推荐：

```python
def login(username, password, role):
    ...
```

不推荐：

```python
def login(a, b, c):
    ...
```

### 5.3 返回值要明确

如果函数是“做动作”，就不要假装它还返回一堆不清楚的结果。

例如：

```python
def open(self):
    self.driver.get(...)
```

如果函数是“取值”，名字和返回值要一致。

例如：

```python
def feedback_text(self):
    return self.driver.find_element(...).text
```

---

## 6. 类和页面对象规范

### 6.1 页面对象负责什么

页面对象更适合负责：

- 页面定位
- 页面动作
- 页面结果读取

例如：

```python
class LoginPage:
    def open(self):
        ...

    def login(self, username, password, role):
        ...

    def feedback_text(self):
        ...
```

### 6.2 页面对象不适合负责什么

不建议把下面这些全塞进页面对象：

- 全部业务断言
- 全部测试分支
- 大量和页面无关的工具逻辑

一句话记住：

`页面对象负责动作，测试负责断言。`

### 6.3 页面对象里的 locator 建议

简单练习阶段可以直接写：

```python
self.driver.find_element(By.ID, "day4-username")
```

如果页面元素多了，建议提成类属性：

```python
class LoginPage:
    USERNAME_INPUT = (By.ID, "day4-username")
    PASSWORD_INPUT = (By.ID, "day4-password")
    ROLE_SELECT = (By.ID, "day4-role")
    LOGIN_BUTTON = (By.ID, "day4-login")
```

这样修改定位时只改一处。

---

## 7. pytest 代码规范

### 7.1 fixture 命名

fixture 名尽量直接表达它提供什么。

推荐：

```python
@pytest.fixture
def driver():
    ...

@pytest.fixture
def base_url():
    ...

@pytest.fixture
def screenshot_dir():
    ...
```

### 7.2 fixture 里的局部变量不要和 fixture 同名

语法上可以，但不推荐。

不推荐：

```python
@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()
```

推荐：

```python
@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()
```

### 7.3 测试函数命名

测试函数用 `test_` 开头，并体现测试目标。

推荐：

```python
def test_login_success(driver):
    ...

def test_login_failed_with_wrong_password(driver):
    ...
```

不推荐：

```python
def test1():
    ...

def login_test():
    ...
```

### 7.4 参数化命名

参数名要能一眼看懂含义。

推荐：

```python
@pytest.mark.parametrize(
    "username, password, role, expected_success",
    [...]
)
```

---

## 8. 等待与断言规范

### 8.1 不要到处乱加 sleep

不推荐：

```python
time.sleep(3)
```

推荐优先使用显式等待：

```python
wait.until(EC.visibility_of_element_located((By.ID, "welcome-message")))
```

### 8.2 等待和断言分开

等待负责：

- 页面状态稳定

断言负责：

- 结果是否符合预期

推荐：

```python
wait.until(EC.url_contains("day4_dashboard"))
assert "欢迎你" in driver.find_element(By.ID, "welcome-message").text
```

### 8.3 断言要断业务结果，不要只断“没报错”

不推荐：

```python
assert True
```

推荐：

```python
assert "登录失败" in login_page.feedback_text()
assert driver.current_url.endswith("day4_login.html")
```

---

## 9. 异常处理规范

### 9.1 不要无脑 try/except

不推荐：

```python
try:
    ...
except Exception:
    pass
```

这会把真正的问题吞掉。

### 9.2 只捕获你真的知道怎么处理的异常

推荐：

```python
from selenium.common.exceptions import ElementClickInterceptedException

try:
    ...
except ElementClickInterceptedException:
    ...
```

### 9.3 资源回收放到 finally 或 yield 后面

推荐：

```python
try:
    ...
finally:
    driver.quit()
```

或者：

```python
@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()
```

---

## 10. 注释规范

### 10.1 注释解释“为什么”，不要解释“这行在赋值”

不推荐：

```python
# 给变量赋值
username = "tester"
```

推荐：

```python
# 失败截图统一落到固定目录，方便排查和归档
screenshot_dir.mkdir(parents=True, exist_ok=True)
```

### 10.2 注释不要太多

如果代码本身已经很清楚，就别再写重复解释。

---

## 11. 配置和数据规范

### 11.1 配置不要到处写死

像 URL、账号、密码、角色这类配置，建议集中管理。

推荐：

```python
BASE_URL = "http://127.0.0.1:8000"
USERNAME = "tester"
PASSWORD = "Selenium123"
ROLE = "qa"
```

### 11.2 测试数据和业务逻辑分开

如果后面参数化数据越来越多，建议单独整理，而不是直接写在大段测试逻辑中。

---

## 12. 类型注解规范

### 12.1 可以加，但先服务于可读性

推荐：

```python
from selenium.webdriver.remote.webdriver import WebDriver

driver: WebDriver = webdriver.Edge()
```

如果类型注解让代码更清楚，就加。  
如果只是为了“显得专业”，但自己也看不懂，就先别堆太多。

---

## 13. 代码风格上的几个常见坏味道

### 13.1 变量名太模糊

```python
data = ...
info = ...
temp = ...
```

### 13.2 一个函数做太多事

```python
def login_and_assert_and_screenshot_and_log(...):
    ...
```

### 13.3 到处复制相同定位

```python
driver.find_element(By.ID, "day4-login")
driver.find_element(By.ID, "day4-login")
driver.find_element(By.ID, "day4-login")
```

### 13.4 页面对象和测试逻辑混在一起

### 13.5 到处乱写硬编码 URL 和账号

---

## 14. 自动化测试场景下的额外建议

1. 页面对象方法尽量短小
2. 登录、搜索、提交这类动作优先封装
3. 等待条件尽量写业务相关的，不要只等元素存在
4. 失败截图路径统一
5. 浏览器生命周期统一交给 fixture
6. 成功和失败断言不要混成一套

---

## 15. 一份你现在就能直接照着用的最小标准

如果你现在还不想记太多，先按这套做就够了：

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://127.0.0.1:8000/pages/day4_login.html")

    def login(self, username, password, role):
        self.driver.find_element(By.ID, "day4-username").clear()
        self.driver.find_element(By.ID, "day4-username").send_keys(username)
        self.driver.find_element(By.ID, "day4-password").clear()
        self.driver.find_element(By.ID, "day4-password").send_keys(password)
        Select(self.driver.find_element(By.ID, "day4-role")).select_by_value(role)
        self.driver.find_element(By.ID, "day4-login").click()

    def feedback_text(self):
        return self.driver.find_element(By.ID, "login-feedback").text
```

这段代码为什么算“合格”：

- 类名规范
- 方法名规范
- 参数名清楚
- 导入只导了用到的内容
- 页面动作和读取分开
- 没有乱写异常处理

---

## 16. 最后记一句

好的 Python 代码规范，不是为了让代码“看起来高级”，而是为了让你：

- 三天后自己回来还能看懂
- 一个月后改起来不痛苦
- 别人接手时不用猜

如果你愿意，我下一步可以继续给你补一份：

`pytest + Selenium 项目代码规范`

那份会更聚焦：

- `conftest.py`
- `fixture`
- `hook`
- `POM`
- 目录结构
- 断言和截图规范
