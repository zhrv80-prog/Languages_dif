import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Обработчик командной строки, который считывает из командной строки параметр language

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=en,
                     help="Choose langauge")

#Логика запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)
