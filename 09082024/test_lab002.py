import By
import driver
from selenium import webdriver

def test_open_vbologin():
    driver = webdriver.Edge()
    driver.get('https://app.vwo.com/#/login')
    print(driver.title)
    print(driver.session_id)
    assert driver.title == 'Login - VWO'
email_element = driver.find_element(By.ID, "login-username")

