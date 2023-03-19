from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # неявное ожидание (ищем каждый элемент, к которому обращаемся до 5 секунд, проверяя каждый 0.5мс)
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    # ожидаем, пока цена станет 100 баксов
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By. ID, 'price'), '100')
    )
    # нажимаем кнопку book, чтобы заказать 
    button = browser.find_element(By.ID, 'book').click()
    # получаем значение параметра х, представляем его в виде текста и используем это значение в функции, которую определили в самом начале программы
    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    y = calc(x)
    # вводим в инпут рассчитанное значение
    browser.find_element(By.ID, 'answer').send_keys(y)
    # нажимаем кнопку подтверждения
    browser.find_element(By.ID, 'solve').click() 

finally:
    time.sleep(5)
    browser.quit()
