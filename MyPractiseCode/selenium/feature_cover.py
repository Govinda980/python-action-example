from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver (Ensure the correct path to your driver)
driver = webdriver.Chrome()
driver.maximize_window()

# Open a website
driver.get("https://www.google.com")

# Explicit wait example
wait = WebDriverWait(driver, 10)

# Finding elements
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for search results
wait.until(EC.presence_of_element_located((By.ID, "result-stats")))

# Clicking a link
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
link.click()

# Handling alerts
try:
    alert = wait.until(EC.alert_is_present())
    print(alert.text)
    alert.accept()
except:
    print("No alert present")

# Handling dropdowns
dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
dropdown.select_by_visible_text("Option 1")

# Handling checkboxes and radio buttons
checkbox = driver.find_element(By.ID, "checkbox_id")
checkbox.click()
radio = driver.find_element(By.ID, "radio_id")
radio.click()

# Handling frames
driver.switch_to.frame("frame_name")
frame_element = driver.find_element(By.TAG_NAME, "p")
print(frame_element.text)
driver.switch_to.default_content()

# Handling multiple windows
main_window = driver.current_window_handle
driver.execute_script("window.open('https://example.com', '_blank');")
time.sleep(2)
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        print("Switched to new tab")
        driver.close()
driver.switch_to.window(main_window)

# Handling cookies
driver.add_cookie({"name": "test_cookie", "value": "test_value"})
cookies = driver.get_cookies()
print("Cookies:", cookies)

# Taking a screenshot
driver.save_screenshot("screenshot.png")

# Scrolling down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Implicit wait example
driver.implicitly_wait(5)

# Closing the browser
driver.quit()