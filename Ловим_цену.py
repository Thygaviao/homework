from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    knopkabook = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    knopkabook.click()
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_xpath('//*[@id="solve"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()