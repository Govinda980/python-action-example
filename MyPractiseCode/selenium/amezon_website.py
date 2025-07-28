import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(10)
element_to_hover = driver.find_element(By.CLASS_NAME, "nav-line-1-container")
actions = ActionChains(driver)
# Perform hover action
actions.move_to_element(element_to_hover).perform()

time.sleep(5)
# Optionally, interact with elements that appear after hover
submenu = driver.find_element(By.CLASS_NAME, "nav-action-inner")
submenu.click()
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("+919739859141")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="continue"]/span/input').click()
# Close the browser
time.sleep(4)

driver.find_element(By.NAME, "password").send_keys("Romeo@2054")
time.sleep(4)

driver.find_element(By.ID, "signInSubmit").click()

time.sleep(4)


driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Redmi 13")
driver.implicitly_wait(5)
mobile = driver.find_element(By.ID, "nav-search-submit-button")
mobile.click()
mobile.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()