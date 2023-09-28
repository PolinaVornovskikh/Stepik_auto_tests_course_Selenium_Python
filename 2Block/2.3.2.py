from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

#Примеры
alert = browser.switch_to.alert
alert.accept()

alert = browser.switch_to.alert
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.accept()
#Отмена
confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
#prompt.dismiss()