from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     link = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_id('input_value')
#     x = x_element.text
#     y = calc(x)
#     input1 = browser.find_element_by_id('answer')
#     input1.send_keys(y)
#     checkbox = browser.find_element_by_css_selector('body > div > form > div.form-check.form-check-custom > label')
#     checkbox.click()
#     radiobutton = browser.find_element_by_css_selector('body > div > form > div.form-check.form-radio-custom > label')
#     radiobutton.click()
#     button = browser.find_element_by_css_selector('body > div > form > button')
#     button.click()
# Код выше для явного значения X

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_x = browser.find_element_by_id('treasure')
    x = element_x.get_attribute('valuex')
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_css_selector('body > div > form > div > div > button')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()