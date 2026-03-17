from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: WebDriver = webdriver.Edge()
driver.get("http://127.0.0.1:8000/pages/day3.html")

# 点击“开始动态加载”
start_loading = driver.find_element(By.ID, "start-loading")
start_loading.click()

# 等待结果文本出现
wait = WebDriverWait(driver, 10)
wait.until(
    EC.text_to_be_present_in_element((By.ID, "delayed-message"), "Hello Day 3")
)

# 打印 `delayed-message` 文本
print(driver.find_element(By.ID, "delayed-message").text)

# 对结果文本做断言
assert " Day 3" in driver.find_element(By.ID, "delayed-message").text

#点击“3 秒后启用按钮”
enable_action = driver.find_element(By.ID, "enable-action")
enable_action.click()

# 等待按钮变为可点击
wait.until(
    EC.element_to_be_clickable((By.ID, "delayed-action"))
)

# 点击按钮
delayed_action = driver.find_element(By.ID, "delayed-action")
delayed_action.click()

# 打印 `action-result`
print(driver.find_element(By.ID, "action-result").text)

# 断言 `data-clicked=true`
assert driver.find_element(By.ID, "action-result").get_attribute("data-clicked") == "true"

# 先拿到一个 `rebuild-item`
item_A = driver.find_element(By.XPATH, '//*[@id="rebuild-list"]/li[1]')

# 点击“重渲染列表”
driver.find_element(By.ID, "rerender-list").click()

# 观察旧元素引用访问失败
# print(item_A.text)

# 重新定位并打印新列表项文本
print(driver.find_element(By.XPATH, '//*[@id="rebuild-list"]/li[1]').text)





driver.quit()