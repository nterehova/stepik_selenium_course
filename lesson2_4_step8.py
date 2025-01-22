from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# ссылка
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_book = browser.find_element(By.ID, "book")
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        
    button_book.click()
    
    time.sleep(1)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer_input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer_input.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()
