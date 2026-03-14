import os

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
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

        button = driver.find_element(By.ID, "covered-button")

        try:
            button.click()
        except ElementClickInterceptedException:
            print("首次点击被拦截：覆盖层还没有消失。")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "blocking-overlay")))
        driver.find_element(By.ID, "covered-button").click()

        result = driver.find_element(By.ID, "covered-result").text
        assert "按钮点击成功" in result
        print("覆盖层状态：已消失")
        print("结果文本：", result)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
