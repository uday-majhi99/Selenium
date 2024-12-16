from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome()

#macimizing window
driver.maximize_window()

#getting an url in a browser
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#checking title
title = driver.title
assert "OrangeHRM" in title
if title == "OrangeHRM":
    print("Test passed")
else:
    print("Test failed")

wait = WebDriverWait(driver,10)

username = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
username.send_keys("Admin")
username.send_keys(Keys.TAB)

password = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Password']")))
password.send_keys("admin123")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Login']")))
login_button.click()

screenshot = "Hrmhome.png"
driver.save_screenshot(screenshot)
if os.path.exists(screenshot):
    print(f"Screenshot has been saved with {screenshot}")
else:
    print("Screenshot has not been saved")

sidebar_shut = wait.until(EC.element_to_be_clickable((By.XPATH,"//i[@class='oxd-icon bi-chevron-left']")))
sidebar_shut.click()

time.sleep(3)

sidebar_open = wait.until(EC.element_to_be_clickable((By.XPATH,"//i[@class='oxd-icon bi-chevron-right']")))
sidebar_open.click()

time.sleep(2)

admin = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]")))
admin.click()
for _ in range(10):  # Adjust the range based on how far you want to scroll
    # Scroll down by 1000 pixels
    driver.execute_script("window.scrollBy(0, 1000);")

    # Wait for the page to load more content
    time.sleep(1)  # Wait for 1 second between scrolls
time.sleep(2)

PIM = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='PIM']")))
PIM.click()
time.sleep(2)

Leave = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Leave']")))
Leave.click()
time.sleep(2)

Time = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]")))
Time.click()
time.sleep(2)

Recruitement = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Recruitment']")))
Recruitement.click()
time.sleep(2)

MyInfo = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='My Info']")))
MyInfo.click()
time.sleep(2)

Performance = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Performance']")))
Performance.click()
time.sleep(2)

Dashboard = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Dashboard']")))
Dashboard.click()
time.sleep(2)

Directory = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Directory']")))
Directory.click()
time.sleep(2)

Claim = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Claim']")))
Claim.click()
time.sleep(2)

Buzz = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Buzz']")))
Buzz.click()
time.sleep(2)

Maintenance = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Maintenance']")))
Maintenance.click()
time.sleep(2)

driver.back()

logout = wait.until(EC.element_to_be_clickable((By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")))
logout.click()
time.sleep(3)

out = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Logout']")))
out.click()

time.sleep(5)

driver.quit()
