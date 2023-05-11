import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.login
def test_check_correct_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"c:\Users\Maryna\KarmazinaQAauto\ " + "chromedriver.exe")
        )
        

    # Відкриваю сторінку http://the-internet.herokuapp.com/login
    driver.get("http://the-internet.herokuapp.com/login")

    # Знаходимо поле, в яке будемо вводити ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "username")

    # Вводимо правильне ім'я користувача або поштову адресу
    login_elem.send_keys("tomsmith")

    # Знаходимо поле, в яке будемо вводити пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо правильний пароль
    pass_elem.send_keys("SuperSecretPassword!")

    # Знаходимо кнопку sing in
    btn_elem = driver.find_element(By.CLASS_NAME, "radius")

    # Емулюємо клік лівою кнопкою миші 
    btn_elem.click()

    # Перевіряємо, що назва сторінки очікувана
    print(driver.title)
    assert driver.title == "The Internet"

    time.sleep(5)

    # Закриваємо браузер
    driver.close()


    