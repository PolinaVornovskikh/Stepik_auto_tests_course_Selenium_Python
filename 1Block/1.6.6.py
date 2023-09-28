import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import webdriver_manager
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium import webdriver

#link1 = "https://www.degreesymbol.net/"
page = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(page)

    #примеры
    #link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
    #link.click()

    #А если хотим найти элемент со ссылкой по подстроке,тj нужно написать следующий код:

    #link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
    #link.click()

    #задание
    f = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #224592
    print(f)
    #link = browser.find_element(By.LINK_TEXT, "224592")
    link = browser.find_element(By.LINK_TEXT, f)
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

