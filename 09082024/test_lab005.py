from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def test_open_vbologin():
    driver = webdriver.Chrome()
    driver.get("https://youtube.com")
    driver.maximize_window()

