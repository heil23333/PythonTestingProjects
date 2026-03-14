import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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

        driver.find_element(By.ID, "start-loading").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.ID, "delayed-message"), "Hello Day 3"))

        print("加载状态：", driver.find_element(By.ID, "loading-pill").text)
        print("结果文本：", driver.find_element(By.ID, "delayed-message").text)
        print("data-ready：", driver.find_element(By.ID, "delayed-message").get_attribute("data-ready"))
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
