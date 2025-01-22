from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# ссылка
link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")
    a = int(a_element.text)
    b = int(b_element.text)
    y = str(a + b)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    
finally:
    time.sleep(20)
    browser.quit()
