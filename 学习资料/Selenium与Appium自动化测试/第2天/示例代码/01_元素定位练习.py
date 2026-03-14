import os

from selenium import webdriver
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
        driver.get(f"{BASE_URL}/pages/day2.html")

        print("标题：", driver.find_element(By.ID, "loc-title").text)
        print("段落：", driver.find_element(By.CSS_SELECTOR, '[data-testid="summary-note"]').text)
        print("链接文本：", driver.find_element(By.LINK_TEXT, "跳转到交互区").text)
        print("第一个 skill：", driver.find_element(By.CLASS_NAME, "skill-item").text)
        print("层级文本：", driver.find_element(By.XPATH, '//div[@id="nested-container"]/p').text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
