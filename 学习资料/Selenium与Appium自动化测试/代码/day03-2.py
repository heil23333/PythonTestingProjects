from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

driver: WebDriver = webdriver.Edge()
driver.get("http://127.0.0.1:8000/pages/day3.html")
wait = WebDriverWait(driver, 10)

# 打开 Day 3 页面后，立即尝试点击 `covered-button`
try:
    driver.find_element(By.ID, "covered-button").click()
except ElementClickInterceptedException:
    # 等待 `blocking-overlay` 消失, 以及`covered-button`可点击
    wait.until(
        EC.invisibility_of_element_located((By.ID, "blocking-overlay"))
    )
    wait.until(
        EC.element_to_be_clickable((By.ID, "covered-button"))
    ).click()

# 断言结果文本变成“覆盖层移除后，按钮点击成功。”
assert driver.find_element(By.ID, "covered-result").text == "覆盖层移除后，按钮点击成功。"

driver.quit()