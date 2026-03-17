import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.tools import save_failure_screenshot

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.parametrize(
    "username, password, role, expected_success",
    [
        ("tester", "Selenium123", "qa", True),
        ("heli", "123456", "dev", False),
        ("", "Selenium123", "dev", False),
        ("tester", "", "pm", False)
    ]
)
def test_login_success(driver, username, password, role, expected_success):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password, role)

    wait = WebDriverWait(driver, 10)

    if expected_success:
        wait.until(EC.url_contains("day4_dashboard"))
        dashboard_page = DashboardPage(driver)
        
        assert "欢迎你" in dashboard_page.welcome_text()
    else:
        save_failure_screenshot(driver, "login_fail")
        assert True == wait.until(EC.text_to_be_present_in_element_attribute((By.ID, "login-feedback"), "data-status", "error"))
        assert "登录失败" in login_page.feedback_text()


