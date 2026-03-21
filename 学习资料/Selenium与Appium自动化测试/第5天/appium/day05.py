from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "AYLNT4OJ79SOOJCI"
options.app_package = "com.android.settings"
options.app_activity = "com.android.settings.Settings"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 10)
view = wait.until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[11]/android.widget.RelativeLayout'))
)
view.click()