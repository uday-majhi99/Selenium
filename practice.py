from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")

driver.maximize_window()

time.sleep()

driver.quit()