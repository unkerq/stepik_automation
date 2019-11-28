from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element_by_name('firstname')
    firstName.send_keys('Vasya')

    lastName = browser.find_element_by_name('lastname')
    lastName.send_keys('Pupkin')

    email = browser.find_element_by_name('email')
    email.send_keys('vasya@pupkin.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

    fileInput = browser.find_element_by_id('file')
    fileInput.send_keys(file_path)

        button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
