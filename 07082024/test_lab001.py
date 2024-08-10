from selenium import webdriver

# Sample code to verify installation
driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and added to PATH
driver.get('https://www.google.com')
print(driver.session_id)

