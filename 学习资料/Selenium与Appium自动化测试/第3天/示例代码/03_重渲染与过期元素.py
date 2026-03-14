import os

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions


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
        driver.get(f"{BASE_URL}/pages/day3.html")

        old_item = driver.find_element(By.CSS_SELECTOR, "#rebuild-list .rebuild-item")
        print("重渲染前：", old_item.text)

        driver.find_element(By.ID, "rerender-list").click()

        try:
            print("尝试访问旧元素：", old_item.text)
        except StaleElementReferenceException:
            print("捕获到 StaleElementReferenceException：旧元素引用已失效。")

        new_item = driver.find_element(By.CSS_SELECTOR, "#rebuild-list .rebuild-item")
        print("重渲染后：", new_item.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
