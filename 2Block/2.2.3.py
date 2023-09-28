from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "num1")
    x = input1.text
    print(x)
    input2 = browser.find_element(By.ID, "num2")
    y = input2.text
    print(y)
    z = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

