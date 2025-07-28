import time
from functools import wraps

from selenium import webdriver
from selenium.webdriver.common.by import By


# Decorator to measure execution time
def measure_time(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time:.4f} seconds")
        return result
    return wrapper


# Apply the decorator to a Selenium function
@measure_time
def open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)  # Simulating some delay
    driver.quit()

# @measure_time
# def search_google():
#     driver = webdriver.Chrome()
#     driver.get("https://www.google.com")
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys("Selenium Python")
#     search_box.submit()
#     time.sleep(3)  # Simulating some wait for results
#     driver.quit()

# Run the functions
open_google()
# search_google()

