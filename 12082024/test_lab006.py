import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_open_vbologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()


# Access element by ID and name are mostly same. And send key in second line
    email_element = driver.find_element(By.ID, "login-username")
    email_element.send_keys("kasar.siddhesh1111@gmail.com")

# Access element byname and send keys into it in one line
    password_element = driver.find_element(By.Name, "Password").send_keys("Sid@1122")

# Access element by CSS selector
    submit_element = driver.find_element(By.CSS, "[data-qa='sibequkica']")
    submit_element.click()
