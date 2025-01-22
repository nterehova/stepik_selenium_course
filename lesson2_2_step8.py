from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# ссылка
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("test@test.com")
    
    input_file = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'upload_file.txt')
    input_file.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    #print(os.path.abspath(__file__))
    #print(os.path.abspath(os.path.dirname(__file__)))
    
finally:
    time.sleep(10)
    browser.quit()
