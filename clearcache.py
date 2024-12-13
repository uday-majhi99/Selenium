from selenium import webdriver
import time
import os
import shutil

driver = webdriver.Chrome()

cache_path = os.path.expanduser('~/.wdm')  #Clear Cache

if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    print(f"Cache at {cache_path} deleted.")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

title = driver.title
print(title)

assert "OrangeHRM" in title
if title == "OrangeHRM":
    print("Assertion Passed")
else:
    print("Assertion Failed")

time.sleep(10)

driver.quit()