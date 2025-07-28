from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to ChromeDriver if necessary
chrome_driver_path = r'C:\Python\pythonProject\selenium\chromedriver-win64\chromedriver.exe'  # Change this if needed

# Launch WebDriver (if chromedriver is in PATH, no need to specify executable_path)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Print the first result title
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
print("First Result Title:", first_result.text)

# Close browser
driver.quit()
