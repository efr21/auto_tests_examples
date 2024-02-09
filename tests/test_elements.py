import time

# from pages.base_page import BasePage
#
#
# def test(driver):
#     page = BasePage(driver, 'https://google.com')
#     page.open()
#     time.sleep(5)
#

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            driver.execute_script("window.scrollTo(0, 200)")  # чтобы кнопка submit была видна
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_address, output_perm_address = text_box_page.check_filled_form()
            assert full_name == output_name, "the full_name does not match"    # через запятую пишем сообщение об ошибке, если она произойдет
            assert email == output_email, "email does not match"
            assert current_address == output_curr_address, "the curr_address does not match"
            assert permanent_address == output_perm_address, "the perm_address does not match"
