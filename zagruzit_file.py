from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
    name.send_keys('Kirill')
    lastname = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    lastname.send_keys('NeKirill')
    mail = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
    mail.send_keys('KirillneKirill@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()