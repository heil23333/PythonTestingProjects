from pathlib import Path

def save_failure_screenshot(driver, name):
    screenshot_dir = Path("artifacts/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(str(screenshot_dir/f"{name}.png"))