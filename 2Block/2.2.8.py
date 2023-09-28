from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[required].form-control[name='firstname']")
    input1.send_keys("y")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[required].form-control[name='lastname']")
    input2.send_keys("y")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[required].form-control[name='email']")
    input3.send_keys("y@h")

    # получаем путь к директории текущего исполняемого скрипта
    # 2.2.8.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "file.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
