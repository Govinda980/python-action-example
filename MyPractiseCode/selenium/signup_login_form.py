from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/register.php")
driver.maximize_window()
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "logo-desktop")))
# time.sleep(10)
driver.implicitly_wait(10)
driver.find_element(By.ID, "firstname").send_keys("Govinda")
driver.find_element(By.ID, "lastname").send_keys("Gupta")
driver.find_element(By.ID, "username").send_keys("Riyansh")
driver.find_element(By.ID, "password").send_keys("Romeo@2054")

time.sleep(3)
driver.find_element(By.CLASS_NAME, "btn-primary").click()


print("Going for login")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Back to Login").click()
time.sleep(2)

driver.find_element(By.ID, "email").send_keys("govindakg543@gmail.com")
driver.find_element(By.ID, "password").send_keys("Romeo@2054")
driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(2)

driver.quit()


