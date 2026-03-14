# Selenium 与 Appium 本地练习站

这套本地练习站用于配合 `Selenium 与 Appium 6 天速成计划` 中的 Web 自动化部分。

它不是一个“最小空页面”，而是按每天的学习目标拆出来的练习环境。

目前已覆盖：

- `Day 1`：自动化入门与首个脚本
- `Day 2`：元素定位与页面交互
- `Day 3`：等待机制、断言、异常排查
- `Day 4`：pytest 项目化与 POM

## 1. 启动方式

建议先创建虚拟环境，再启动本地服务。

在项目根目录执行：

```bash
cd '练习项目/Selenium与Appium本地练习站'
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python app/app.py
```

启动后访问：

- 健康检查：`http://127.0.0.1:8000/health`
- 首页：`http://127.0.0.1:8000/index.html`
- Day 1：`http://127.0.0.1:8000/pages/day1.html`
- Day 2：`http://127.0.0.1:8000/pages/day2.html`
- Day 3：`http://127.0.0.1:8000/pages/day3.html`
- Day 4：`http://127.0.0.1:8000/pages/day4_login.html`

## 2. 每天覆盖内容

### Day 1

页面：`pages/day1.html`

可练内容：

- 打开页面
- 定位文本输入框
- 输入内容
- 点击提交按钮
- 获取提交结果文本
- 关闭浏览器

### Day 2

页面：`pages/day2.html`

可练内容：

- `id / name / class name / tag name / link text / css / xpath`
- 输入、清空、点击
- 获取文本
- 获取属性
- `is_displayed()` 和 `is_enabled()`

### Day 3

页面：`pages/day3.html`

可练内容：

- 动态内容出现
- 按钮延迟可点击
- 元素重新渲染
- 等待结果文本变化
- 基础断言和常见异常观察

### Day 4

页面：`pages/day4_login.html`、`pages/day4_dashboard.html`

可练内容：

- 登录成功/失败流程
- 参数化测试
- fixture 驱动复用
- 页面对象模型
- 登录页与结果页分层封装

## 3. 建议使用方式

建议按课程顺序使用：

1. Day 1 先只操作 `day1.html`
2. Day 2 再切到 `day2.html`
3. Day 3 再练动态页面和等待
4. Day 4 用登录页和仪表盘页练 `pytest + POM`

## 4. 说明

- 这套页面由项目内的 Python 服务托管，后续可以继续补登录、接口、动态数据等教学场景。
- 当前服务不依赖第三方包，使用 Python 标准库即可运行。
- 这套页面是为 Selenium 练习设计的，不是生产级业务站点。
- 页面刻意保留了稳定的 `id`、`name`、`class`、`data-testid` 等属性，方便你练定位。
- 如果后续课程进入移动端实战，我会继续补 Android/iOS 对应练习环境规范和代码骨架。
