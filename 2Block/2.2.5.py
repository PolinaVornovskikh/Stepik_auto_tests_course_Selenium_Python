from selenium import webdriver
from selenium.webdriver.common.by import By

#пример 1
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
#button = browser.find_element(By.TAG_NAME, "button")
#button.click()


#пример 2
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#пример 3
#browser.execute_script("window.scrollBy(0, 100);")

#пример 4
#// javascript
#button = document.getElementsByTagName("button")[0];
#button.scrollIntoView(true);
