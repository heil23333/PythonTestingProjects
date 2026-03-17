from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://127.0.0.1:8000/pages/day4_login.html")

    def login(self, username, password, role):
        self.driver.find_element(By.ID, "day4-username").clear()
        self.driver.find_element(By.ID, "day4-username").send_keys(username)
        self.driver.find_element(By.ID, "day4-password").clear()
        self.driver.find_element(By.ID, "day4-password").send_keys(password)
        Select(self.driver.find_element(By.ID, "day4-role")).select_by_value(role)
        self.driver.find_element(By.ID, "day4-login").click()

    def feedback_text(self):
        return self.driver.find_element(By.ID, "login-feedback").text