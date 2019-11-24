from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element_by_id("treasure")
    x = box.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

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



