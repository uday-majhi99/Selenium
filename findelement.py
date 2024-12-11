from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.geeksforgeeks.org/interacting-with-webpage-selenium-python/?ref=next_article')
driver.maximize_window()
searchIcon = driver.find_element(By.ID,'gcse-search-input')
searchIcon.click()
time.sleep(10)