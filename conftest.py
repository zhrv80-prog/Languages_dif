import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Обработчик командной строки, который считывает из командной строки параметр language


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "#login_link")

#Логика запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
