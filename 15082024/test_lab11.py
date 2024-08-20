#implicit Wait example
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_implicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    email_element = driver.find_element(By.CSS_SELECTOR, 'input#login-username')
    password_element = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

    email_element.send_keys("kasar.siddhesh1111@gmail.com")
    password_element.send_keys("Sid") #in valid password to check error message

    driver.find_element(By.CSS_SELECTOR, 'button#js-login-btn').click()


    time.sleep(5)
    error_message = driver.find_element(By.CSS_SELECTOR, 'div[data-qa="rixawilomi"]').text
    assert error_message == 'Your email, password, IP address or location did not match'