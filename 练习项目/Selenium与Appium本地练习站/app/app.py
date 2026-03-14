from __future__ import annotations

import json
import mimetypes
import os
import time
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self._send_json({"status": "ok", "app": "selenium-appium-lab"})
            return

        if parsed.path == "/api/day3/result":
            params = parse_qs(parsed.query)
            delay_ms = self._safe_int(params.get("delay", ["2500"])[0], 2500)
            time.sleep(max(delay_ms, 0) / 1000)
            self._send_json({
                "ready": True,
                "message": "Hello Day 3，动态内容已经出现。",
            })
            return

        if parsed.path == "/api/day3/enable":
            params = parse_qs(parsed.query)
            delay_ms = self._safe_int(params.get("delay", ["3000"])[0], 3000)
            time.sleep(max(delay_ms, 0) / 1000)
            self._send_json({
                "enabled": True,
                "message": "按钮已可点击。",
            })
            return

        self._serve_static(parsed.path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        body = self._read_payload()

        if parsed.path == "/api/day1/submit":
            name = (body.get("name") or "").strip() or "同学"
            role = (body.get("role") or "").strip() or "Selenium 初学者"
            self._send_json({
                "ok": True,
                "message": f"提交成功：{name}，欢迎进入 {role} 的第一个自动化练习。",
            })
            return

        if parsed.path == "/api/day4/login":
            username = (body.get("username") or "").strip()
            password = (body.get("password") or "").strip()
            role = (body.get("role") or "").strip()

            if username == "tester" and password == "Selenium123" and role == "qa":
                self._send_json({
                    "ok": True,
                    "redirect": "/pages/day4_dashboard.html",
                    "user": {
                        "username": username,
                        "role": role,
                    },
                })
                return

            self._send_json({
                "ok": False,
                "message": "登录失败：用户名、密码或角色不正确。",
            }, status=HTTPStatus.UNAUTHORIZED)
            return

        self._send_json({"ok": False, "message": "unknown endpoint"}, status=HTTPStatus.NOT_FOUND)

    def _read_payload(self) -> dict[str, str]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length) if length else b""
        content_type = self.headers.get("Content-Type", "")

        if "application/json" in content_type:
            try:
                return json.loads(raw.decode("utf-8")) if raw else {}
            except json.JSONDecodeError:
                return {}

        parsed = parse_qs(raw.decode("utf-8"))
        return {key: values[0] for key, values in parsed.items()}

    def _serve_static(self, request_path: str) -> None:
        path = request_path or "/"
        if path == "/":
            path = "/index.html"

        relative = path.lstrip("/")
        target = (PROJECT_ROOT / relative).resolve()

        if PROJECT_ROOT not in target.parents and target != PROJECT_ROOT:
            self.send_error(HTTPStatus.FORBIDDEN, "Forbidden")
            return

        if not target.exists() or not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return

        content_type, _ = mimetypes.guess_type(str(target))
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type or "application/octet-stream")
        self.end_headers()
        self.wfile.write(target.read_bytes())

    def _send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    @staticmethod
    def _safe_int(raw: str, default: int) -> int:
        try:
            return int(raw)
        except ValueError:
            return default


def main() -> None:
    port = int(os.environ.get("APP_PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), LabHandler)
    print(f"Selenium 与 Appium 本地练习站已启动: http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
