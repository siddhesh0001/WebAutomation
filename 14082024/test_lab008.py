#Xpath example

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_xpath_case():
    driver = webdriver.Chrome()
    driver.get("https://rhn.accucia.co/profile")
    driver.maximize_window()

    abb = driver.find_element(By.XPATH, "//button[@type='button']") #this is Xpath
    abb.click()
    time.sleep(2)