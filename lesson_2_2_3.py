from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    option1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    option1.send_keys("name")

    option2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    option2.send_keys("lastname")

    option3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    option3.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.CSS_SELECTOR, '[id="file"]')
    element.send_keys(file_path)

    
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)

finally:
    time.sleep(5)
    browser.quit()