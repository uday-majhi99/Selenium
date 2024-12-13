from selenium import webdriver
import time
import os
import shutil

driver = webdriver.Chrome()

cache_path = os.path.expanduser('~/.wdm')

if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    print(f"Cache in path {cache_path} cleared successfully")

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(10)

driver.quit()