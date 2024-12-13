from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

title = driver.title
print("Title for the page is : "+title)

assert "OrangeHRM" in title
if title == "OrangeHRM":
    print("Assertion passed")
else:
    print("Assertion failed")

time.sleep(10)

driver.quit()
