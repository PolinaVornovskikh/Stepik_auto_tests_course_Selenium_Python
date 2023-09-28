from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    print(x)
    y = str(math.log(abs(12 * math.sin(int(x)))))
    print(y)

    browser.execute_script("window.scrollBy(0, 150);")

    input2 = browser.find_element(By.CSS_SELECTOR, "input[required].form-control")
    input2.send_keys(y)
    checkb = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkb.click()
    radiob = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiob.click()
    # required_elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    # for element in required_elements:
    # element.send_keys("1")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()