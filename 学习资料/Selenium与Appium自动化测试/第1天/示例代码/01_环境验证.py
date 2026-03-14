import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        driver.get(f"{BASE_URL}/pages/day1.html")
        print("页面标题：", driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
