from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try: 
   browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
   message = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100" ))

   button = browser.find_element(By.ID, "book")
   button.click()

   x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
   x = x_element.text
   y = calc(x)

   option1 = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
   option1.send_keys(y)
   button = browser.find_element(By.ID, "solve")
   button.click()

finally: 
   time.sleep(5)
   browser.quit()