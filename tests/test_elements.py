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
            #  driver.execute_script("window.scrollTo(0, 200)") - чтобы кнопка submit была видна
            text_box_page.fill_all_fields()
            output_name, output_email, output_curr_address, output_perm_address = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_curr_address)
            print(output_perm_address)
