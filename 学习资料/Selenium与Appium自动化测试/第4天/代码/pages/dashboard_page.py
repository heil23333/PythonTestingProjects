from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def welcome_text(self):
        return self.driver.find_element(By.ID, "welcome-message").text

    def role_value(self):
        return self.driver.find_element(By.ID, "role-badge").get_attribute("data-role")