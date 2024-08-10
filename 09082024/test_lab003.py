from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vbologin():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x800")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://app.vwo.com/#/login')