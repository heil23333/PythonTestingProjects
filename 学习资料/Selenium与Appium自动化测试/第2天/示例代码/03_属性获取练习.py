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

        username = driver.find_element(By.ID, "login-username")
        link = driver.find_element(By.ID, "practice-link")
        note = driver.find_element(By.CSS_SELECTOR, '[data-testid="summary-note"]')
        checkbox = driver.find_element(By.ID, "agree-policy")

        print("id：", username.get_attribute("id"))
        print("name：", username.get_attribute("name"))
        print("type：", username.get_attribute("type"))
        print("placeholder：", username.get_attribute("placeholder"))
        print("class：", note.get_attribute("class"))
        print("data-testid：", note.get_attribute("data-testid"))
        print("href：", link.get_attribute("href"))
        print("复选框是否勾选：", checkbox.is_selected())

        checkbox.click()
        print("点击后复选框是否勾选：", checkbox.is_selected())
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
