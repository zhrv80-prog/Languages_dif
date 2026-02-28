#Тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

#Открыть страницу http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        #Ищем элемент
        button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket[value='Добавить в корзину']")  
        """
        если с ожиданием  
        button1 = WebDriverWait(browser, 10).until(
                                                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket"))
                                                )
        """
        #Сам элемент вот такой 
        #<button type="submit" class="btn btn-lg btn-primary btn-add-to-basket" value="Добавить в корзину" data-loading-text="Добавление...">Добавить в корзину</button>
        
        print(button1.text)

        button_found = True
    except NoSuchElementException:
        button_found = False

    assert button_found

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
