from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_window_size(2560,1600)

driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(2)