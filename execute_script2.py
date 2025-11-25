from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import re

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()  # chromedriver должен быть в PATH
try:
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # 2. считываем x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 3. считаем y
    y = calc(x)

    # 4 & 5. прокрутка до поля и ввод ответа
    answer_input = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_input)
    time.sleep(0.3)
    answer_input.send_keys(y)

    # 6. чекбокс
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 7. радиокнопка
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # 8. прокрутить к кнопке и нажать
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(0.2)
    submit_btn.click()

    # получить текст alert и извлечь число
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Alert text:", alert_text)
    
    nums = re.findall(r"[-+]?\d+\.?\d*", alert_text)
    if nums:
        print("Искомое число (первое найденное):", nums[0])
    else:
        print("Число в alert не найдено явно.")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
