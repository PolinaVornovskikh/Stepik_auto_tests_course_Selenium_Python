from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    print(x)
    y = str(math.log(abs(12 * math.sin(int(x)))))
    print(y)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    buttonsub = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    buttonsub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()