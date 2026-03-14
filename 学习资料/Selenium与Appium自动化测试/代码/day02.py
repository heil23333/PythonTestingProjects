from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver: WebDriver = webdriver.Edge()
driver.get("http://127.0.0.1:8000/pages/day2.html")

# 使用 By.ID 找到用户名输入框并输入内容
username = driver.find_element(By.ID, "login-username")
username.send_keys("测试用户名")
print(username.text)

# 使用 `By.NAME` 找到密码输入框并输入内容
password = driver.find_element(By.NAME, "password")
password.send_keys("123456")
print(password.text)

# 点击“提交登录表单”
submit_button = driver.find_element(By.ID, "submit-login")
submit_button.click()

# 打印状态文本
login_status = driver.find_element(By.ID, "login-status")
print(login_status.text)

# 点击“填充演示值”
fill_demo = driver.find_element(By.ID, "fill-demo")
print(fill_demo.text)

# 读取用户名输入框的 value
print(username.get_attribute("value"))

# 点击“清空用户名”
clear_username = driver.find_element(By.ID, "clear-username")
clear_username.click()

# 再次读取用户名输入框的 `value`
print(username.get_attribute("value"))

# 读取 `attribute-status` 的文本
attribute_status = driver.find_element(By.ID, "attribute-status")
print(attribute_status.text)

# 读取用户名输入框的 `placeholder`
print(username.get_attribute("placeholder"))

# 读取“跳转到交互区”链接的 `href`
practice_link = driver.find_element(By.ID, "practice-link")
print(practice_link.get_attribute("href"))

# 判断协议复选框的勾选状态
agree_policy = driver.find_element(By.ID, "agree-policy")
print(agree_policy.is_selected)

# 用 `Select` 把目标阶段切到 `Day 3`
select_el = driver.find_element(By.ID, 'target-level')
select = Select(select_el)
select.select_by_index(1)

# 打印当前下拉框选中的文本和值
print(select.first_selected_option.text)
print(select.first_selected_option.get_attribute("value"))

# 跳转到交互区
print(driver.find_element(By.ID, "practice-link"))
print(driver.find_element(By.LINK_TEXT, "跳转到交互区"))
print(driver.find_element(By.CSS_SELECTOR, "#practice-link"))
print(driver.find_element(By.XPATH, '//*[@id="practice-link"]'))

# data-*练习
locator_note = driver.find_element(By.CSS_SELECTOR, '[data-testid="summary-note"]')
print(locator_note.text)
print(driver.find_element(By.XPATH, '//p[@data-testid="summary-note"]').text)

# print(driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div[1]/p").text)
# print(driver.find_element(By.ID, "practice-link").text)
# print(driver.find_element(By.XPATH, '//*[@id="tag-box"]/span[3]').text)
# print(driver.find_element(By.CSS_SELECTOR, '#skills-list > li:nth-child(3)').get_attribute("data-skill"))
# driver.find_element(By.LINK_TEXT, "跳转到交互区").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "交互区").click()
# driver.find_element(By.ID, "fill-demo").click()

# print(driver.find_element(By.XPATH, '//*[@id="attribute-status"]').text)
# driver.find_element(By.ID, "clear-username").click()
# driver.find_element(By.NAME, "username").send_keys("heli")
# driver.find_element(By.ID, "submit-login").click()
# print(driver.find_element(By.ID, "login-status").text)
# print(driver.find_element(By.ID, "agree-policy").is_selected())

# driver.find_element(By.ID, "agree-policy").click()
# driver.find_element(By.ID, "submit-login").click()
# print(driver.find_element(By.ID, "login-status").text)

# driver.find_element(By.ID, "login-username").clear()
# driver.find_element(By.NAME, "username").send_keys("hefanbei")
# driver.find_element(By.ID, "radio-java").click()
# driver.find_element(By.ID, "submit-login").click()
# print(driver.find_element(By.ID, "login-status").text)

# select_el = driver.find_element(By.ID, 'target-level')
# select = Select(select_el)
# select.select_by_index(2)
# print(driver.find_element(By.ID, "login-username").get_attribute("placeholder"))
# print(select_el.get_attribute("value"))
# print(driver.find_element(By.ID, "agree-policy").is_selected())

driver.quit()