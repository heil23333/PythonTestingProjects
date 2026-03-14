import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.select import Select


BASE_URL = "http://127.0.0.1:8000"


def build_driver():
    browser = os.environ.get("SELENIUM_BROWSER", "chrome").lower()

    if browser == "edge":
        options = EdgeOptions()
        if os.environ.get("SELENIUM_HEADLESS") == "1":
            options.add_argument("--headless=new")
        return webdriver.Edge(options=options)

    if browser == "safari":
        return webdriver.Safari()

    options = Options()
    if os.environ.get("SELENIUM_HEADLESS") == "1":
        options.add_argument("--headless=new")

    return webdriver.Chrome(options=options)


def main() -> None:
    driver = build_driver()
    try:
        driver.get(f"{BASE_URL}/pages/day2.html")

        driver.find_element(By.ID, "fill-demo").click()
        username = driver.find_element(By.ID, "login-username")
        print("填充后的用户名：", username.get_attribute("value"))
        print("用户名占位提示：", username.get_attribute("placeholder"))
        print("填充标记：", username.get_attribute("data-filled"))

        checkbox = driver.find_element(By.ID, "agree-policy")
        checkbox.click()
        print("协议是否已勾选：", checkbox.is_selected())

        driver.find_element(By.ID, "radio-java").click()
        print("Java 单选是否选中：", driver.find_element(By.ID, "radio-java").is_selected())
        select = Select(driver.find_element(By.ID, "target-level"))
        select.select_by_visible_text("Day 3")
        print("当前目标阶段文本：", select.first_selected_option.text)
        print("当前目标阶段值：", select.first_selected_option.get_attribute("value"))
        print("跳转链接地址：", driver.find_element(By.ID, "practice-link").get_attribute("href"))
        driver.find_element(By.ID, "submit-login").click()

        print("提交结果：", driver.find_element(By.ID, "login-status").text)

        driver.find_element(By.ID, "clear-username").click()
        print("清空后的用户名：", username.get_attribute("value"))
        print("属性状态：", driver.find_element(By.ID, "attribute-status").text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
