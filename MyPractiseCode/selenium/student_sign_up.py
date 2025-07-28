from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
# driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Riyansh")
driver.find_element(By.ID, "email").send_keys("govindakg543@gmail.com")
driver.find_element(By.ID, "gender").click()
print("cliclkled..")
driver.find_element(By.ID, "mobile").send_keys("9739859141")
driver.find_element(By.ID, "dob").send_keys("28-03-1998")
driver.find_element(By.ID, "subjects").send_keys("Computer Engineer")
driver.find_element(By.XPATH, '//*[@id="practiceForm"]/div[7]/div/div/div[2]/input').click()
driver.find_element(By.XPATH, '//*[@id="practiceForm"]/div[7]/div/div/div[3]/input').click()
driver.find_element(By.NAME, 'picture').send_keys(r'C:\Python\pythonProject\selenium\Photo\Riyansh.jpg')

driver.find_element(By.ID, "state").send_keys("NCR")
driver.find_element(By.ID, "city").send_keys("Agra")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="practiceForm"]/div[11]/input').click()

# driver.find_element(By.XPATH, '//*[@id="state"]/option[2]').send_keys("NCR")
# driver.find_element(By.XPATH, '//*[@id="picture"]').send_keys("BHEL Township")

time.sleep(10)
driver.quit()
