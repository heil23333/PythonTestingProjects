from selenium.webdriver.common.by import By

class AdvancedPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    def iframe_input_username(self):
        self.driver.switch_to_frame("day4-practice-frame")
        self.driver.find_element(By.ID, "frame-username").send_keys("heli")