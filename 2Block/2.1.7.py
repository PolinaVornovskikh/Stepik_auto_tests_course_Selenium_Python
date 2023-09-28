from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "treasure")
    x = input1.get_attribute("valuex")
    print(x)
    y = str(math.log(abs(12 * math.sin(int(x)))))
    print(y)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
    checkb = browser.find_element(By.ID, "robotCheckbox")
    checkb.click()
    radiob = browser.find_element(By.ID, "robotsRule")
    radiob.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()