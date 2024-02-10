import time
import allure
# from pages.base_page import BasePage
#
#
# def test(driver):
#     page = BasePage(driver, 'https://google.com')
#     page.open()
#     time.sleep(5)
#

from pages.elements_page import TextBoxPage, CheckBoxPage


@allure.suite("Elements")
class TestElements:

    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            driver.execute_script("window.scrollTo(0, 200)")  # чтобы кнопка submit была видна
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_address, output_perm_address = text_box_page.check_filled_form()
            assert full_name == output_name, "the full_name does not match"  # через запятую пишем сообщение об ошибке, если она произойдет
            assert email == output_email, "email does not match"
            assert current_address == output_curr_address, "the curr_address does not match"
            assert permanent_address == output_perm_address, "the perm_address does not match"

    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes have not been selected'
