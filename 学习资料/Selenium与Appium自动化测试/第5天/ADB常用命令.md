# ADB 常用命令

这份小抄主要面向 `Appium / Android` 自动化学习。

重点不是把所有 ADB 命令背全，而是先掌握最常用、最能解决实际问题的那一批。

---

## 1. 设备连接与状态

### 查看 ADB 版本

```bash
adb version
```

### 查看当前连接设备

```bash
adb devices
```

这是最常用的一条。  
如果设备没有出现在这里，后面的 `Appium` 基本也跑不起来。

### 启动 / 重启 ADB 服务

```bash
adb start-server
adb kill-server
```

设备识别异常、连接状态奇怪时很常用。

---

## 2. 无线调试

### Android 11 及以上：先配对，再连接

```bash
adb pair IP:配对端口
adb connect IP:调试端口
```

注意：

- `pair` 用的是配对端口
- `connect` 用的是调试端口
- 这两个端口不一定相同

### 断开无线连接

```bash
adb disconnect
adb disconnect IP:端口
```

---

## 3. 设备与系统信息

### 查看 Android 版本

```bash
adb shell getprop ro.build.version.release
```

### 查看设备型号

```bash
adb shell getprop ro.product.model
```

### 查看屏幕分辨率

```bash
adb shell wm size
```

### 查看屏幕密度

```bash
adb shell wm density
```

---

## 4. 安装、卸载、启动 App

### 安装 APK

```bash
adb install app.apk
```

### 覆盖安装

```bash
adb install -r app.apk
```

### 卸载 App

```bash
adb uninstall 包名
```

### 查看所有已安装包

```bash
adb shell pm list packages
```

### 按关键字查包名

```bash
adb shell pm list packages | grep 关键字
```

### 启动指定 App

```bash
adb shell monkey -p 包名 -c android.intent.category.LAUNCHER 1
```

这条很适合：

- 你知道包名
- 但暂时不知道入口 `Activity`

### 精确启动指定 Activity

```bash
adb shell am start -n 包名/Activity全名
```

### 强制停止 App

```bash
adb shell am force-stop 包名
```

### 清空 App 数据

```bash
adb shell pm clear 包名
```

这条很适合把 App 重置到“首次安装”状态。

---

## 5. 查包名和 Activity

### 查当前前台页面

```bash
adb shell dumpsys window | grep mCurrentFocus
```

这条很常用，适合：

- 看当前打开的是哪个页面
- 辅助判断当前 `Activity`

### 解析启动 Activity

```bash
adb shell cmd package resolve-activity --brief 包名
```

### 查看可启动入口

```bash
adb shell pm dump 包名 | grep -A 1 MAIN
```

---

## 6. 模拟点击、输入、按键

### 点击坐标

```bash
adb shell input tap x y
```

### 输入文本

```bash
adb shell input text hello
```

### 返回键

```bash
adb shell input keyevent 4
```

### Home 键

```bash
adb shell input keyevent 3
```

### 回车键

```bash
adb shell input keyevent 66
```

### 滑动

```bash
adb shell input swipe x1 y1 x2 y2 300
```

最后一个数字通常是持续时间，单位毫秒。

---

## 7. 常见 keyevent

| keyevent | 含义 |
|---|---|
| `3` | Home |
| `4` | Back |
| `26` | 电源键 |
| `66` | Enter |
| `82` | Menu |

---

## 8. 日志、截图、录屏

### 查看日志

```bash
adb logcat
```

### 按关键字过滤日志

```bash
adb logcat | grep 包名
```

### 截图并拉到电脑

```bash
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png
```

### 录屏并拉到电脑

```bash
adb shell screenrecord /sdcard/demo.mp4
adb pull /sdcard/demo.mp4
```

---

## 9. 文件传输

### 推文件到手机

```bash
adb push 本地文件 设备路径
```

例子：

```bash
adb push demo.txt /sdcard/Download/
```

### 从手机拉文件到电脑

```bash
adb pull 设备文件 本地路径
```

例子：

```bash
adb pull /sdcard/Download/demo.txt .
```

---

## 10. 进入设备 Shell

### 进入交互式 shell

```bash
adb shell
```

### 直接执行一条 shell 命令

```bash
adb shell ls /sdcard/Download
```

---

## 11. 端口转发

### 本地访问设备端口

```bash
adb forward tcp:本地端口 tcp:设备端口
```

### 让设备访问电脑端口

```bash
adb reverse tcp:设备端口 tcp:本地端口
```

这类命令在调试本地服务、Hybrid 场景或特殊联调时有用。

---

## 12. 做 Appium 时最常用的几条

如果你现在只想先记最常用的一批，就记下面这些：

```bash
adb devices
adb shell pm list packages
adb shell pm list packages | grep 关键字
adb shell dumpsys window | grep mCurrentFocus
adb shell monkey -p 包名 -c android.intent.category.LAUNCHER 1
adb shell am force-stop 包名
adb shell pm clear 包名
adb logcat
```

---

## 13. 建议记忆顺序

建议按这个顺序掌握：

1. `adb devices`
2. `adb shell pm list packages`
3. `adb shell dumpsys window | grep mCurrentFocus`
4. `adb shell monkey -p 包名 -c android.intent.category.LAUNCHER 1`
5. `adb shell am force-stop 包名`
6. `adb shell pm clear 包名`
7. `adb logcat`
8. `adb shell input tap`
9. `adb shell input swipe`

先把这 9 条用熟，你做 Day 5 / Day 6 的 Appium 学习就已经很够用了。
