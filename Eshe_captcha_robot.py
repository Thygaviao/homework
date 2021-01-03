from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(element_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_xpath('/html/body/div/form/div[2]/label')
    checkbox.click()
    radiobutton = browser.find_element_by_xpath('/html/body/div/form/div[4]/label')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


# Код выше для явного значения X
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()