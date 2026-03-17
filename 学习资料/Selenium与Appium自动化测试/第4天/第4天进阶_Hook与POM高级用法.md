# Selenium 与 Appium 自动化测试 Day 4 进阶：Hook 与 POM 高级用法

## 1. 这份进阶资料适合什么时候看

这份文档不是 Day 4 主线的“必背内容”，而是给你在下面这些时候看的：

- 你已经能写最基本的 `pytest + selenium` 登录用例
- 你已经理解了 `fixture`、参数化和最小 `POM`
- 你开始想知道：
  - 为什么很多项目会写 `conftest.py`
  - 为什么失败截图常常用 `hook`
  - 为什么有些 `POM` 越写越乱
  - 页面对象到底该管到哪一层

如果你现在还在熟悉：

- `yield`
- `driver` fixture
- `pytest.mark.parametrize`

那建议先以 Day 4 主线为主，这份文档可以边查边看，不需要一次看完。

---

## 2. 这份进阶文档到底解决什么问题

Day 4 主线解决的是：

- 能把 Selenium 脚本写成 `pytest` 用例
- 能用 `fixture`
- 能做参数化
- 能开始拆 `POM`

这份进阶解决的是：

1. `fixture` 再往前一步怎么组织
2. `hook` 是什么，它和 `fixture` 到底怎么配合
3. 失败自动截图为什么常放在 `hook`
4. `POM` 高级一点应该怎么分层
5. 哪些封装是“真的有帮助”，哪些是“看起来高级，实际更乱”

你可以把它理解成：

`从“会用”走向“会设计”的第一步。`

---

## 3. 先把 Day 4 主线和进阶边界分清

### 3.1 Day 4 主线要求掌握什么

- 测试函数怎么写
- `fixture` 怎么提供浏览器
- 参数化怎么让一条测试跑多组数据
- 页面对象怎么抽最基本的页面动作

### 3.2 这份进阶要求理解什么

- `fixture` 的 scope、依赖、拆分方式
- `conftest.py` 为什么是 pytest 项目里的关键文件
- `hook` 为什么属于“时机扩展”，而不是“资源准备”
- `POM` 怎么避免越写越臃肿
- 页面对象、组件对象、断言、等待应该怎么分边界

### 3.3 先记一句总原则

`主线先会跑，进阶再会设计。`

很多人反过来学，最后就会变成：

- 会说一堆概念
- 目录结构很复杂
- 但真正的测试却没几条能稳定跑通

---

## 4. fixture 进阶：它不只是“浏览器启动器”

Day 4 主线里，你已经见过最基本的浏览器 `fixture`：

```python
@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()
```

现在进阶要解决的问题是：

- 一个项目里可以有不止一个 fixture
- fixture 之间还可以互相依赖
- 它们不只提供浏览器，还可以提供页面对象、测试数据、目录路径

### 4.1 fixture 的真正职责

你可以把 fixture 的职责总结成两句：

1. 给测试提供公共资源
2. 统一资源的创建和清理方式

所以除了 `driver`，下面这些都可以是 fixture：

- `base_url`
- `login_page`
- `dashboard_page`
- `screenshot_dir`
- `valid_user`

例如：

```python
import pytest
from pathlib import Path


@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"


@pytest.fixture
def screenshot_dir():
    folder = Path("artifacts/screenshots")
    folder.mkdir(parents=True, exist_ok=True)
    return folder
```

这里你要看懂的是：

- fixture 不一定都要 `yield`
- 如果它只是返回一个简单值，也可以直接 `return`

### 4.2 什么时候用 return，什么时候用 yield

如果 fixture 只是提供一个“值”：

```python
@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"
```

那用 `return` 就够了。

如果 fixture 要管理“需要回收的资源”：

```python
@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()
```

那就更适合用 `yield`。

你可以先记：

- `return`：只提供值
- `yield`：提供资源，并在后面做清理

### 4.3 fixture 之间还能依赖

这点很重要，也是很多人第一次觉得 pytest 很顺的地方。

例如：

```python
@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()


@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"


@pytest.fixture
def login_page(driver, base_url):
    return LoginPage(driver, base_url)
```

这里表示：

- `login_page` 这个 fixture 自己不造浏览器
- 它依赖 `driver`
- 也依赖 `base_url`
- 最后返回一个页面对象

这就是 pytest 的一个核心特点：

`fixture 也可以依赖 fixture。`

### 4.4 随堂检查

1. fixture 只能提供浏览器吗？
2. fixture 什么时候更适合用 `yield`？
3. fixture 之间能不能互相依赖？

### 4.5 答案

1. 不能，它还可以提供页面对象、测试数据、目录路径等公共资源。
2. 当它管理的是需要回收的资源时，例如浏览器、数据库连接、临时文件。
3. 可以。

---

## 5. fixture 的 scope 进阶：为什么不是越大越好

你前面已经知道 `scope` 决定 fixture 活多久。

常见值有：

- `function`
- `class`
- `module`
- `session`

### 5.1 为什么 UI 自动化默认更推荐 function

因为 UI 自动化特别容易互相污染。

例如前一个测试可能会留下：

- 已登录状态
- 表单残留值
- 弹窗未关闭
- sessionStorage 未清空
- URL 停在错误页面

如果你用：

```python
@pytest.fixture(scope="session")
def driver():
    ...
```

虽然浏览器只开一次，看起来快了，但你很容易遇到：

- A 用例影响 B 用例
- 某条失败后，后面整串都不稳定

所以 Day 4 主线先用 `function` 是对的。

### 5.2 那大 scope 什么时候有用

在这些场景里，大 scope 才开始有价值：

- 启动资源成本特别高
- 资源是只读的、不容易污染
- 你已经有很成熟的清理逻辑

例如：

- 一个很慢的 API client
- 一套初始化数据
- 某些只读配置对象

对浏览器来说，大 scope 并不是不能用，只是对学习阶段和大多数 UI 测试来说，风险更高。

### 5.3 一句经验话

`scope 不是性能优化按钮，它首先是隔离策略。`

### 5.4 随堂检查

1. 为什么浏览器 fixture 在 Day 4 不推荐一开始就上 `session`？
2. scope 先考虑的是速度，还是隔离？

### 5.5 答案

1. 因为浏览器状态很容易污染后续测试，隔离性比少开几次浏览器更重要。
2. 先考虑隔离。

---

## 6. conftest.py 进阶：它为什么是 pytest 项目的骨架

很多人第一次看到 `conftest.py` 会觉得它只是“一个放 fixture 的文件”。

这个理解只对了一半。

更准确地说：

`conftest.py` 是 pytest 在某个目录层级下的公共配置入口。`

它常常用来放：

- 共享 fixture
- hook
- 公共路径或工具

### 6.1 它的核心价值

如果你把浏览器 fixture 写在：

```python
tests/test_login.py
```

那通常只有这个文件能直接用。

如果你把它写到：

```python
conftest.py
```

那同目录及子目录下的测试都能直接用，不用手动 import。

### 6.2 一个更像项目的 Day 4 conftest.py

```python
import pytest
from pathlib import Path
from selenium import webdriver


@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"


@pytest.fixture
def screenshot_dir():
    folder = Path("artifacts/screenshots")
    folder.mkdir(parents=True, exist_ok=True)
    return folder


@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()
```

这份文件的意义是：

- 以后所有测试都统一从这里拿公共资源
- 浏览器怎么起、截图目录怎么放，不再散在各个测试文件里

### 6.3 conftest.py 里应该少放什么

不要把下面这些东西全堆进去：

- 所有业务逻辑
- 所有页面对象
- 一大堆和测试无关的工具函数

你可以记成：

- `conftest.py`：放测试基础设施
- `pages/`：放页面对象
- `tests/`：放测试场景

### 6.4 随堂检查

1. `conftest.py` 的核心价值是什么？
2. 页面对象适不适合全都塞进 `conftest.py`？

### 6.5 答案

1. 让共享 fixture 和 hook 能在目录范围内被自动发现和复用。
2. 不适合。

---

## 7. hook 到底是什么：它和 fixture 的边界怎么分

这是你前面问得最多的一块，我们这次详细拆开。

### 7.1 hook 的一句话定义

`hook 是 pytest 在固定时机留给你的扩展点。`

也就是：

- 测试收集时
- 测试执行前
- 测试执行后
- 生成测试结果时

你可以插入自己的逻辑。

### 7.2 fixture 和 hook 的边界

你可以直接记这组对比：

- `fixture`：管资源
- `hook`：管时机

换成更口语化的话：

- fixture 负责“给你什么”
- hook 负责“什么时候做”

放到失败截图这个例子里：

- fixture 提供 `driver`
- hook 在“测试失败”这个时机自动去截图

### 7.3 为什么 hook 不适合 Day 4 主线

因为它有两个门槛：

1. 你得先理解 pytest 的执行阶段
2. 你得先理解 fixture 是怎么把资源塞进测试函数的

如果这两个前置概念都还没稳，hook 很容易只剩下“抄一段能跑的代码”。

所以现在你要把它理解成：

`pytest 的流程扩展能力`

而不是“Day 4 必须掌握的基础语法”。

### 7.4 随堂检查

1. hook 更偏向管资源，还是管时机？
2. 失败截图为什么常常是 fixture 和 hook 配合做？

### 7.5 答案

1. 管时机。
2. 因为截图需要 fixture 提供浏览器，又需要 hook 在失败时机自动触发。

---

## 8. pytest_runtest_makereport 详细拆解

失败自动截图最常见的 hook 就是：

```python
def pytest_runtest_makereport(item, call):
    ...
```

它的作用是：

`在一条测试运行后，让你拿到这条测试的结果。`

### 8.1 最小示例

```python
import pytest
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return

        folder = Path("artifacts/screenshots")
        folder.mkdir(parents=True, exist_ok=True)
        driver.save_screenshot(str(folder / f"{item.name}.png"))
```

### 8.2 逐行看懂这段代码

```python
@pytest.hookimpl(hookwrapper=True)
```

这行的意思是：

- 下面这个函数是 pytest 的一个 hook 实现
- `hookwrapper=True` 表示我们想“包一层” pytest 原本的执行过程

你现在先不必死记这个参数，只要知道：

- 它让你可以先 `yield`
- 等 pytest 把这次测试跑完
- 再回来拿结果

```python
outcome = yield
report = outcome.get_result()
```

这两行的作用是：

- 先把控制权交回 pytest
- 等这条测试真正执行完成
- 再拿到执行报告 `report`

这里的 `report` 很关键，因为它告诉你：

- 这条测试在哪个阶段
- 成功还是失败

```python
if report.when != "call":
    return
```

pytest 一条测试通常分 3 个阶段：

- `setup`
- `call`
- `teardown`

这里我们只关心测试主体，也就是 `call`。

因为很多时候你说的“测试失败”，其实你真正想关注的是：

- 测试逻辑里的断言失败
- 测试主体执行失败

而不是 setup 或 teardown 的一些辅助失败。

```python
if report.failed:
```

只有失败了，才继续做截图。

```python
driver = item.funcargs.get("driver")
```

这行非常重要。

它的意思是：

- 看这条测试函数有没有使用 `driver` 这个 fixture
- 如果用了，就把这个浏览器对象拿出来

这也是为什么 hook 和 fixture 会配合得这么自然。

### 8.3 item.funcargs 是什么

你可以先把它理解成：

`这条测试当前可用的 fixture 实参字典`

例如测试函数是：

```python
def test_login(driver, base_url):
    ...
```

那你就可以在 hook 里通过：

- `item.funcargs["driver"]`
- `item.funcargs["base_url"]`

拿到这些资源。

### 8.4 为什么不是每个 hook 都适合你一开始就学

因为 hook 不是“写测试”必需的第一层。

更准确地说：

- fixture 是“基础设施”
- hook 是“扩展能力”

先有前者，再学后者，顺序才不会乱。

### 8.5 随堂检查

1. `pytest_runtest_makereport` 最常见的用途是什么？
2. `report.when == "call"` 在过滤什么？
3. `item.funcargs.get("driver")` 在取什么？

### 8.6 答案

1. 在测试执行后拿到测试结果，做失败截图、附加日志等处理。
2. 在过滤 setup 和 teardown，只保留测试主体阶段。
3. 在取这条测试所使用的 `driver` fixture 实例。

---

## 9. 自动失败截图：为什么它常常被放在 hook 里

先看不用 hook 时的做法：

```python
def test_login(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_login.html")
    driver.save_screenshot("fail.png")
    assert False
```

这当然能截图，但问题是：

- 每条测试都要自己写
- 很容易忘
- 风格不统一

而如果放到 hook 里：

- 所有测试失败都会自动截图
- 路径统一
- 命名规则统一

所以 hook 更适合“全局统一动作”。

### 9.1 自动截图最容易踩的坑

1. 测试没用 `driver`，hook 却硬拿 `driver`
2. 截图目录没提前创建
3. 测试在 setup 阶段失败，结果你误以为是测试主体失败
4. 截图文件名重复，被后面的截图覆盖

### 9.2 更稳一点的命名方式

如果你后面要增强，可以这样写：

```python
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"{item.name}_{timestamp}.png"
```

这样重复覆盖的概率会小很多。

### 9.3 一句经验话

`hook 适合做“每次都要统一执行”的事情。`

比如：

- 自动截图
- 附加失败日志
- 测试完成后收集元数据

---

## 10. pytest-selenium 插件进阶：它和自己写 fixture 的关系

你前面已经问到这个插件，我们这里把位置摆清楚。

### 10.1 它是干什么的

`pytest-selenium` 会直接给你提供一个 `selenium` fixture。

例如：

```python
def test_login_success(selenium):
    selenium.get("http://127.0.0.1:8000/pages/day4_login.html")
```

然后运行时通常这样指定浏览器：

```bash
pytest --driver Edge
```

### 10.2 它的优点

- 上手快
- 浏览器驱动管理更方便
- 和 pytest 风格融合得比较自然

### 10.3 它的代价

你会更晚接触到底层细节，例如：

- 浏览器实例到底是谁创建的
- fixture 生命周期是谁在控制
- 什么时候该自己扩展 driver fixture

所以最合理的顺序通常是：

1. 先会写纯 `pytest + selenium`
2. 再用 `pytest-selenium` 提高效率

### 10.4 什么时候更适合自己写 fixture

当你需要：

- 自定义浏览器 options
- 更复杂的 driver 创建逻辑
- 更明确地控制生命周期
- 和自己的页面对象、截图目录、日志系统组合

自己写 fixture 往往更直观。

---

## 11. POM 进阶：页面对象为什么常常越写越乱

很多人学到 `POM` 后，容易走两个极端：

1. 什么都不封装，测试文件里全是裸 `find_element`
2. 什么都往页面对象里塞，最后页面对象变成一个巨大工具箱

真正好的 `POM` 不在这两个极端里。

### 11.1 POM 的核心职责

POM 真正最有价值的事情是：

- 收拢定位
- 收拢页面动作
- 提高测试可读性

它不是为了：

- 把所有逻辑都装进 class
- 把所有断言都藏起来
- 把所有等待都抽成神秘基类

### 11.2 一个坏味道示例

```python
class LoginPage:
    def do_everything(self, username, password, role):
        ...
        ...
        ...
```

这种方法名就已经在提醒你：

- 它做得太多了

常见坏味道包括：

- 一个方法既输入数据、又点击、又断言、又截图
- 页面对象里塞满业务判断分支
- 页面对象直接操作别的页面

### 11.3 一条实用边界线

你可以先这样分：

- 页面对象：页面动作和页面读取
- 测试函数：场景组合和业务断言

例如：

```python
page.login(username, password, role)
assert "登录失败" in page.feedback_text()
```

这里：

- `login()` 是页面动作
- `feedback_text()` 是页面读取
- `assert ...` 是测试逻辑

边界就很清楚。

### 11.4 随堂检查

1. POM 的核心价值是什么？
2. 页面对象里适不适合塞大量业务断言？

### 11.5 答案

1. 收拢定位和页面动作，提高可维护性和可读性。
2. 一般不适合。

---

## 12. POM 进阶：等待应该放在哪里

这是写页面对象时最容易迷糊的一点。

### 12.1 完全不放等待，会有什么问题

如果页面对象里完全不处理等待：

```python
def click_login(self):
    self.driver.find_element(By.ID, "day4-login").click()
```

那测试文件里就可能到处补：

- `WebDriverWait`
- `sleep`
- 重复等待逻辑

最后会很散。

### 12.2 所有等待都塞进页面对象，又有什么问题

如果你把所有等待都藏进页面对象，测试就会变成：

- 表面上很短
- 但真正发生了什么不透明

例如：

```python
page.login(...)
page.wait_for_everything()
page.ensure_page_ready()
```

这类命名如果不清晰，后面维护会很痛苦。

### 12.3 更稳的 Day 4 进阶建议

把等待分两类：

1. 页面动作的基本稳定性等待
2. 测试场景的业务结果等待

页面动作层面可以放少量等待，例如：

```python
def click_login(self):
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "day4-login"))
    ).click()
```

这是“页面动作能顺利执行”的等待。

但像这种：

```python
wait.until(EC.url_contains("day4_dashboard"))
```

更像是“业务结果成立”的等待，放在测试函数里通常更清晰。

### 12.4 一句经验话

`动作稳定性交给页面对象，业务结果判断留给测试。`

---

## 13. POM 进阶：BasePage 要不要上

很多教程一讲 `POM` 就会先建一个 `BasePage`。

这个做法不是错，但很容易被滥用。

### 13.1 什么时候 BasePage 有价值

当你真的有这些重复时：

- 每个页面都要 `open`
- 每个页面都要统一等待方法
- 每个页面都要统一截图方法
- 每个页面都要统一查找方法

那抽一个最小 `BasePage` 是合理的。

例如：

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
```

### 13.2 什么时候不要急着上 BasePage

如果你现在只有：

- 2 个页面对象
- 几个方法
- 重复还不多

那可以先不抽，等重复明显再说。

因为很多人的 `BasePage` 会慢慢变成：

- 一个什么都往里塞的超级类
- 一堆你自己都不确定什么时候该用的方法

### 13.3 一个判断标准

`先有真实重复，再抽共性；不要为了“看起来完整”提前建过大的基类。`

---

## 14. POM 进阶：页面对象和组件对象

当页面变复杂时，只有“页面对象”这一层有时不够。

例如一个页面里可能有：

- 顶部导航栏
- 左侧菜单
- 登录弹窗
- 表格组件

这时可以再拆一层“组件对象”。

### 14.1 什么是组件对象

它表示：

`页面中的一个可复用局部区域。`

比如：

```python
class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.ID, "logout-button").click()
```

然后页面对象里组合它：

```python
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.header = HeaderComponent(driver)
```

这层在 Day 4 不是必须，但你要先知道这个方向。

它适合：

- 页面很大
- 某些区块在多个页面复用

不适合：

- 页面很小
- 你只是为了“多拆几层看起来高级”

---

## 15. Day 4 进阶推荐目录结构

如果你要把 Day 4 做得更像一个小项目，可以这样组织：

```text
day4_project/
  pytest.ini
  conftest.py
  pages/
    base_page.py
    login_page.py
    dashboard_page.py
  components/
    header_component.py
  tests/
    test_login.py
  artifacts/
    screenshots/
```

### 15.1 每层负责什么

- `conftest.py`
  - 共享 fixture
  - hook

- `pages/`
  - 页面对象

- `components/`
  - 局部可复用组件

- `tests/`
  - 测试场景和断言

- `artifacts/`
  - 截图、日志、报告等产物

### 15.2 这套结构最容易被写坏的方式

- 把页面对象写成业务断言中心
- 把 hook、fixture、工具函数全塞 `conftest.py`
- 一开始就做太多抽象，实际只写了 2 条测试

---

## 16. 一套“够用但不过度”的进阶实践建议

如果你现在要在 Day 4 的基础上往前走，我建议这个顺序：

1. 先把 `driver`、`base_url`、`screenshot_dir` 做成 fixture
2. 再把 `LoginPage`、`DashboardPage` 稳定下来
3. 然后补一个最小失败自动截图 hook
4. 真的出现重复后，再考虑 `BasePage`
5. 页面变大后，再考虑组件对象

你会发现，这条顺序的核心还是：

`先解决真实问题，再抽象。`

---

## 17. 进阶自测

### 17.1 概念题

1. fixture 和 hook 的核心区别是什么？
2. 为什么失败自动截图通常是 fixture 和 hook 配合？
3. POM 里为什么不建议把所有断言都塞进页面对象？
4. `BasePage` 为什么不建议一开始就做得很大？

### 17.2 代码理解题

看下面代码，回答问题：

```python
@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"artifacts/screenshots/{item.name}.png")
```

请回答：

1. 这段代码里，fixture 负责什么？
2. hook 负责什么？
3. 为什么要判断 `report.when != "call"`？
4. 为什么是 `item.funcargs.get("driver")`，而不是直接写 `driver.save_screenshot(...)`？

### 17.3 标准答案

1. fixture 负责提供并回收浏览器资源。
2. hook 负责在测试完成后查看结果，并在失败时执行统一截图逻辑。
3. 因为要过滤掉 setup 和 teardown，只关心测试主体阶段。
4. 因为 hook 自己没有现成的浏览器变量，它需要从这条测试实际使用的 fixture 参数里把 driver 取出来。

### 17.4 概念题参考答案

1. fixture 管资源，hook 管时机。
2. 因为截图需要浏览器资源，又需要在失败时机统一触发。
3. 因为页面对象的职责更适合放定位和页面动作，测试断言应该留在测试层。
4. 因为过大的基类会让抽象先于真实需求，后面反而更难维护。

---

## 18. 看完这份文档后，你至少要带走什么

如果你不想一口气全吃下去，那至少带走这 6 句话：

1. `fixture` 管资源，`hook` 管时机。
2. 浏览器 fixture 默认优先用函数级隔离。
3. `conftest.py` 是 pytest 项目的基础设施入口。
4. 页面对象负责动作和读取，测试负责断言。
5. hook 适合做统一的失败截图、日志收集等全局动作。
6. 不要为了显得完整，过早做过大的 `BasePage` 和复杂抽象。
