from selenium import webdriver
import os
import shutil
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

cache_path = os.path.expanduser("~/.wdm")
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    print(f"Cache in path {cache_path} cleared successfully")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
title = driver.title
print(title)
assert "OrangeHRM" in title
if title == "OrangeHRM":
    print("Assertion Passed")
else:
    print("Assertion Failed")

wait = WebDriverWait(driver,10)
username = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
username.send_keys('admin')
username.send_keys(Keys.TAB)

password = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Password']")))
password.send_keys('admin123')

login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
login_button.click()
Screenshot = "HRMpage.png"
driver.save_screenshot(Screenshot)
if os.path.exists(Screenshot):
    print(f"Screenshot saved as {Screenshot}")
else:
    print(f"Screenshot not saved")


title = driver.title
assert "OrangeHRM" in title
if title == "OrangeHRM":
    print("Assertion Passed")
else:
    print("Assertion Failed")

time.sleep(10)

driver.quit()