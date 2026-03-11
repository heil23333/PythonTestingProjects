# 本地接口练习服务

这是给 Python 接口自动化测试 Day 2 准备的本地练习项目。

目标不是做完整后端，而是提供一套稳定、可重复练习的接口环境，让你可以练下面这些能力：

- `requests`
- `requests.get/post/delete`
- `params`
- `json`
- `data`
- 状态码和响应解析
- 登录获取 token
- 携带请求头访问受保护接口

## 项目结构

```text
本地接口练习服务/
├── .venv/
├── app/
│   └── app.py
├── data/
│   └── seed.json
├── scripts/
├── .gitignore
├── README.md
└── requirements.txt
```

## 默认运行地址

```text
http://127.0.0.1:5001
```

## 默认测试账号

- 用户名：`alice`
- 密码：`123456`

## 详细接口文档

[接口文档.md](./接口文档.md)

## 主要接口

- `GET /health`
- `POST /api/v1/debug/reset`
- `POST /api/v1/login`
- `GET /api/v1/profile`
- `GET /api/v1/products`
- `GET /api/v1/products/<id>`
- `POST /api/v1/products`
- `DELETE /api/v1/products/<id>`
- `POST /api/v1/echo-form`

## 启动方式

先创建并激活虚拟环境，再安装依赖：

```bash
cd /Users/Apple/Documents/Codes/PythonTestingProjects/练习项目/本地接口练习服务
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

启动服务：

```bash
python app/app.py
```

服务启动后访问：

```text
http://127.0.0.1:5001/health
```

如果返回 `{"code":0,...}`，说明服务正常。
