from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    num2 = num2_element.text
    num3 = str(int(num1) + int(num2))
    #time.sleep(3)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(num3) # ищем элемент с текстом "Python"
    #time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла