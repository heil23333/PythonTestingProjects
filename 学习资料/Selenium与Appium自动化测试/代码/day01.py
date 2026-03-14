from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Edge()
driver.get("http://127.0.0.1:8000/pages/day1.html")

driver.find_element(By.ID, "day1-name").send_keys("HeLi")
driver.find_element(By.ID, "day1-role").send_keys("自动化测试学习者")

driver.find_element(By.ID, "day1-submit").click()

print(driver.find_element(By.ID, "day1-message").text)

driver.quit()