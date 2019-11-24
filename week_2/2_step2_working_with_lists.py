from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text

    num2 = browser.find_element_by_id("num2").text

    num1digital = int(num1)
    num2digital = int(num2)
    sumdig = num1digital + num2digital

    sum = str(sumdig)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum) # ищем элемент с текстом "Python"

#    checkbox = browser.find_element_by_id('robotCheckbox')
#    checkbox.click()

#    radiobutton = browser.find_element_by_id('robotsRule')
#    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

#    people_radio = browser.find_element_by_id('peopleRule')
#    people_checked = people_radio.get_attribute("checked")
#    print("value of people radio: ", people_checked)
#    assert people_checked == "true", "People radio is not selected by default"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
