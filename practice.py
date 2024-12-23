from selenium import webdriver
import time

# Initialize the driver
driver = webdriver.Chrome()

# Open the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Wait for the page to load completely
time.sleep(5)

# Set the scroll parameters (distance to scroll per step and wait time)
scroll_distance = 50  # Small distance to scroll per step (in pixels)
scroll_pause_time = 1  # Longer pause to make it really slow (in seconds)

# Continuously scroll down slowly
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down by a small amount
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

    # Wait for a bit before scrolling again
    time.sleep(scroll_pause_time)

    # Check the current page height and see if it's reached the bottom
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("Reached the bottom of the page.")
        break  # Stop scrolling when no new content is loaded
    last_height = new_height

# Wait to observe the final scroll action
time.sleep(5)

# Close the browser
driver.quit()
from selenium import webdriver
import time

# Initialize the driver
driver = webdriver.Chrome()

# Open the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Wait for the page to load completely
time.sleep(5)

# Set the scroll parameters (distance to scroll per step and wait time)
scroll_distance = 100  # Small distance to scroll per step (in pixels)
scroll_pause_time = 1  # Longer pause to make it really slow (in seconds)

# Continuously scroll down slowly
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down by a small amount
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

    # Wait for a bit before scrolling again
    time.sleep(scroll_pause_time)

    # Check the current page height and see if it's reached the bottom
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("Reached the bottom of the page.")
        break  # Stop scrolling when no new content is loaded
    last_height = new_height

# Wait to observe the final scroll action
time.sleep(5)

# Close the browser
driver.quit()
