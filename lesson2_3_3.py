'''
Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

button = driver.find_element_by_css_selector("button[type='submit']")
button.click()

new_window = driver.window_handles[1]

driver.switch_to.window(new_window)

time.sleep(1)
x_element = driver.find_element_by_id("input_value")
x = x_element.text

y = str(math.log(abs(12*math.sin(int(x)))))
textarea = driver.find_element_by_id("answer")
textarea.send_keys(y)

driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(1)

'''
button2 = driver.find_element_by_css_selector("button[type='submit']")
button2.click()


time.sleep(1)
driver.close()
driver.quit()
'''
