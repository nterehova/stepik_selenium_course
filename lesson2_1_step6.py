from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# ссылка
link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    # radiobutton
    robots_radio = browser.find_element(By.ID, "robotsRule")

    people_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", people_checked)
    assert people_checked is not None, "Robots radio is not selected by default"

    
finally:
    time.sleep(10)
    browser.quit()
