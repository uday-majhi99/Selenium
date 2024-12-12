from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com/')

driver.maximize_window()

driver.save_screenshot("Google.png")
print("Screenshot saved as Home Page Google")

title = driver.title
print('The title of the webpage is:'+ title)
assert "Google" in title
print("Asserting that the title of the Pass")

time.sleep(3)
