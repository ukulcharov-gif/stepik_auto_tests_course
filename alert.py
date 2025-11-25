from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Ждём кнопку и кликаем
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
    ).click()

    # Переключаемся на confirm
    confirm = WebDriverWait(browser, 10).until(EC.alert_is_present())

    # Смысл: нажимаем OK
    confirm.accept()

    # Ждём появления поля x на новой странице
    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )

    x = x_element.text
    answer = calc(x)

    # Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(answer)

    # Кликаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Ждём появления alert с числом
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    print("Ответ:", alert.text)

finally:
    browser.quit()
