from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    button.click()


#    print("value of people radio: ", people_checked)
#    assert people_checked == "true", "People radio is not selected by default"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
