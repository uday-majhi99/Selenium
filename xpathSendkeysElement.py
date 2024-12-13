from selenium import webdriver
import time
import os
import shutil
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming ChromeDriver is installed)
driver = webdriver.Chrome()

# Clear the cache (if needed)
cache_path = os.path.expanduser('~/.wdm')  # Path to the webdriver manager cache

if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    print(f"Cache in path {cache_path} cleared successfully")

# Open the target URL (OrangeHRM login page)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# Wait until the username field is present and visible before interacting with it
wait = WebDriverWait(driver, 10)
username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))

# Enter the username 'admin' and press TAB to move to the password field
username.send_keys('admin')
username.send_keys(Keys.TAB)

# Wait until the password field is visible and send the password
password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
password.send_keys('admin123')

# Correct XPath for the Login button (submit button)
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# Maximize the window (optional)
driver.maximize_window()

# Wait for a while to observe the result (optional, can be adjusted or removed)
time.sleep(5)

# Close the browser
driver.quit()
