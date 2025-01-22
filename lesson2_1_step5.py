from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# ссылка
link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer_input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer_input.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    option1.click()
    
    # radiobutton
    option2 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()
