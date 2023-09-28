from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    h = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    buttonb = browser.find_element(By.ID, "book")
    buttonb.click()

    browser.execute_script("window.scrollBy(0, 150);")
    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    print(x)
    y = str(math.log(abs(12 * math.sin(int(x)))))
    print(y)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    buttonsub = browser.find_element(By.ID, "solve")
    buttonsub.click()

    #message = browser.find_element(By.ID, "verify_message")

    #assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
