#CSS Selector example we will see

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_CSS_types():
    driver = webdriver.Chrome()
    driver.get("https://rhn.accucia.co/")
    driver.maximize_window()

    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "input[id=':r0:']").click()
    driver.find_element(By.CSS_SELECTOR, "input[id=':r0:']").send_keys("Replace")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "svg[data-testid='ShoppingBagOutlinedIcon']").click()
    time.sleep(2)