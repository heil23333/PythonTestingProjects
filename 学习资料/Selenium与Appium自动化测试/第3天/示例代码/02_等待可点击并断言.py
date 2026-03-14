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

        driver.find_element(By.ID, "enable-action").click()
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, "delayed-action")))
        button.click()

        result = driver.find_element(By.ID, "action-result")
        assert result.get_attribute("data-clicked") == "true"
        print("按钮可用状态：", driver.find_element(By.ID, "delayed-action").is_enabled())
        print("执行结果：", result.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
