from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    #browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    button = browser.find_element(By.CSS_SELECTOR, '[class="trollface btn btn-primary"]')
    button.click()
    time.sleep(1)

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)
    time.sleep(1)

    #confirm = browser.switch_to.alert
    #confirm.accept()
    #time.sleep(1)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)

    option1 = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
    option1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()