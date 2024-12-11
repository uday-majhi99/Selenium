from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.set_window_size(2560,1600)

driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(2)
title = driver.title
print("The title of a page is : " +title)
driver.quit()