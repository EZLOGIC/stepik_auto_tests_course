from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.execute_script("window.scrollBy(0, 100);")

button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "[id = 'input_value']")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button.click()

time.sleep(30)
    
browser.quit()
