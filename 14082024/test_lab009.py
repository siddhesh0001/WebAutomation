#Xapth types we will see
#ie full visbile text and partially visible text
# Also we will see how to combine more than 1 xpath or element

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_xpath_types():
    driver = webdriver.Chrome()
    driver.get("https://rhn.accucia.co/")
    driver.maximize_window()

    time.sleep(5)
    #Full visible text
    driver.find_element(By.XPATH, "//a[text()='Combo offer']").click()
    time.sleep(2)

     #Partial visible text
    driver.find_element(By.XPATH, "//a[contains(text(), 'Buy')]").click()
    time.sleep(2)

     #Combining more than 1 xpath using AND, OR
    driver.find_element(By.XPATH, "//a[text()='Combo offer'] | //a[contains(text(), 'Combo')]").click()
    time.sleep(2)

    #Normal Xpath or tag locator finding.
    driver.find_element(By.XPATH, "//img[@alt = 'Vitamin Combo']").click()
    time.sleep(2)