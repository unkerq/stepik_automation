import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/find_xpath_form")

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
firstname = driver.find_element_by_xpath('//input[@name="first_name"]')
# Напишем текст ответа в найденное поле
firstname.send_keys("first_name")

lastname = driver.find_element_by_xpath('//input[@name="last_name"]')
lastname.send_keys("last_name")

city = driver.find_element_by_xpath('//input[@class="form-control city"]')
city.send_keys("City")

country = driver.find_element_by_xpath('//input[@id="country"]')
country.send_keys("Country")

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_xpath('//button[@type="submit"]')

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(14)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
