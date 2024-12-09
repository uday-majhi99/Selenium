import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (assuming you're using Chrome here)
driver = webdriver.Chrome()

# Open a website (e.g., Google)
driver.get("https://www.google.com")

# Wait for 3 seconds (if you want to pause right after the page loads)
time.sleep(3)

# Locate the search input and enter a search query
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium WebDriver")

# Optionally, you can submit the search
search_input.submit()

# Wait for 3 seconds after the redirection (after submitting)
time.sleep(3)

# If there's another redirection or action after this, add more sleep as needed
# For example, after a click, wait for 3 seconds again
# Example of click and wait:
# some_button = driver.find_element(By.ID, "some_button")
# some_button.click()
# time.sleep(3)

# Close the driver after your work is done
driver.quit()

