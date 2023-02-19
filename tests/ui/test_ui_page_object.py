from modules.ui.page_objects.sing_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкрити сторінку http://github.com/login
    sign_in_page.go_to()

    #Виконати спробу увійти в систему GitHub
    sign_in_page.try_login("marynakarma@gmail.com", "qwerty")

    # Перевіряємо, що назва сторінки очікувана
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    
    # Закриваємо браузер
    sign_in_page.close()