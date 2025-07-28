from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (Make sure you have the correct driver installed)
driver = webdriver.Chrome()

# Open a webpage (replace with the actual URL)
driver.get("https://example.com")

# Locate the button (replace 'button_id' with actual locator)
button = driver.find_element(By.ID, "button_id")

# Check if the button contains "Run" text
if "Run" in button.text:
    print("Button contains 'Run' text.")
else:
    print("Button does not contain 'Run' text.")

# Close the browser
driver.quit()
