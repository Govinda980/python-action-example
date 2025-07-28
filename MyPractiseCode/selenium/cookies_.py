import time
from selenium import webdriver
driver = webdriver.Chrome()

cookies = driver.get_cookies()
print("cookies",cookies)
driver.get("https://mail.google.com/")
driver.add_cookie({"name": "myCookie", "value": "123456"})
time.sleep(10)

for cookie in cookies:
    print(cookie['name'], cookie['value'])