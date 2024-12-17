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
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fclient%3Dfirefox-b-d%26q%3Dgmail&ec=GAZAAQ&hl=en&passive=true&ifkv=AeZLP99B1dDuyLh3Xq0iO2RaDvjv7pvBXcgC8gekWE0OxWKT-jcpKrAkp563QdvRe55tllHH6kktmw&ddm=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

wait = WebDriverWait(driver,10)

username = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='identifierId']")))
username.send_keys("testingdomeinfosys@gmail.com")
#
# password = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Password']")))
# password.send_keys("admin123")
#
Next = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Next']")))
Next.click()

# screenshot = "googlehome.png"
# driver.save_screenshot(screenshot)
# if os.path.exists(screenshot):
#     print(f"Screenshot has been saved with {screenshot}")
# else:
#     print("Screenshot has not been saved")




time.sleep(5)

driver.quit()
