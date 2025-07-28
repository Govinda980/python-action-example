import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
# search_key = driver.find_element(By.ID, "search2")
# search_key.send_keys("Python")
# time.sleep(10)
# search_btn = driver.find_element(By.ID, "learntocode_searchbtn")
#
# search_btn.click()
# search_btn.send_keys(Keys.RETURN)

login_btn = driver.find_element(By.CLASS_NAME,
                                "user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login")
login_btn.click()
email = driver.find_element(By.NAME, "email")
email.send_keys("govindakg543@gmail.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("Romeo@2054")
login = driver.find_element(By.CLASS_NAME,
                            "CustomButton_button__V5-G+ LoginForm_login_button__B4Ksc CustomButton_primary__ZDr5g")
login.click()
