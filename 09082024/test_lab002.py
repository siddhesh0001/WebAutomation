from selenium import webdriver

def test_open_vbologin():
    driver = webdriver.Edge()
    driver.get('https://app.vwo.com/#/login')
    print(driver.title)
    print(driver.session_id)
    assert driver.title == 'Login - VWO'


