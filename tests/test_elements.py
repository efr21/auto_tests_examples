import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://google.com')
    page.open()
    time.sleep(5)  # это пишем, чтобы увидеть, как браузер открывается данную страницу