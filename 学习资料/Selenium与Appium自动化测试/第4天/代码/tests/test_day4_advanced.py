from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_advanced_frame(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    # driver.switch_to.frame("day4-practice-frame")
    wait = WebDriverWait(driver, 5)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "day4-practice-frame")))

    driver.find_element(By.ID, "frame-username").send_keys("heli")
    driver.find_element(By.ID, "frame-submit").click()
    assert "heli" in driver.find_element(By.ID, "frame-result").text

    driver.find_element(By.ID, "frame-fill").click()
    assert "已填充 iframe 示例数据" in driver.find_element(By.ID, "frame-result").text

    driver.switch_to.parent_frame()
    assert "主页面上下文" in driver.find_element(By.ID, "advanced-host-note").text

def test_advanced_alert(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    assert "尚未触发 alert" in driver.find_element(By.ID, "alert-result").text
    driver.find_element(By.ID, "trigger-alert").click()
    alert  = driver.switch_to.alert
    alert.accept()
    assert "accepted" == driver.find_element(By.ID, "alert-result").get_attribute("data-state")
    assert "alert 已处理完成" in driver.find_element(By.ID, "alert-result").text

def test_advanced_confirm(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    assert "尚未触发 confirm" in driver.find_element(By.ID, "confirm-result").text
    driver.find_element(By.ID, "trigger-confirm").click()
    confirm = driver.switch_to.alert
    confirm.accept()
    assert "confirm 结果：你点击了确定。" in driver.find_element(By.ID, "confirm-result").text

    driver.find_element(By.ID, "trigger-confirm").click()
    confirm = driver.switch_to.alert
    confirm.dismiss()
    assert "confirm 结果：你点击了取消。" in driver.find_element(By.ID, "confirm-result").text

def test_advanced_prompt(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    assert "尚未触发 prompt" in driver.find_element(By.ID, "prompt-result").text
    driver.find_element(By.ID, "trigger-prompt").click()
    prompt = driver.switch_to.alert
    prompt.dismiss()
    assert "prompt 结果：你取消了输入。" in driver.find_element(By.ID, "prompt-result").text

    driver.find_element(By.ID, "trigger-prompt").click()
    prompt = driver.switch_to.alert
    print(prompt.text)
    prompt.send_keys("heli")
    prompt.accept()
    assert "prompt 结果：你输入了 heli。" in driver.find_element(By.ID, "prompt-result").text
    assert "heli" == driver.find_element(By.ID, "prompt-result").get_attribute("data-value")

def test_day4_file_upload(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    assert "尚未选择文件。" in driver.find_element(By.ID, "upload-result").text
    driver.find_element(By.ID, "upload-input").send_keys("/Users/Apple/Downloads/雀神榜.csv")
    assert "雀神榜.csv" in driver.find_element(By.ID, "upload-result").text
    assert "selected" == driver.find_element(By.ID, "upload-result").get_attribute("data-state")
    assert "雀神榜.csv" in driver.find_element(By.ID, "upload-result").get_attribute("data-file-name")

def test_day4_download(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")
    
    download_link = driver.find_element(By.ID, "download-template")
    assert "template.txt" in download_link.get_attribute("href")
    assert "" == download_link.get_attribute("download")

def test_day4_switch_tabs(driver):
    driver.get("http://127.0.0.1:8000/pages/day4_advanced.html")

    origin = driver.current_window_handle
    driver.find_element(By.ID, "open-dashboard-tab").click()

    wait = WebDriverWait(driver, 5)
    wait.until(lambda d: len(d.window_handles) == 2)
    new_handle = [h for h in driver.window_handles if h != origin][0]

    driver.switch_to.window(new_handle)
    assert "请先回到登录页" in driver.find_element(By.ID, "welcome-message").text
    assert "dashboard.html" in driver.current_url
    driver.close()

    driver.switch_to.window(origin)
    assert "advanced.html" in driver.current_url