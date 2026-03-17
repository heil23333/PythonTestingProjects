import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def driver():
    browser: WebDriver = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()