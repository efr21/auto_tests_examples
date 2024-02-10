import random

import allure
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):  # наследуемся от BasePage
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(
            generated_person())  # это итератор, он позволяет нам взять ровно по 1 разу full_name, email, address, 1 экземпляр person
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step("filling all fields"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("click submit button"):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()  # кнопка должна быть видима

    # найдя элементы, нам нужно на них кликнуть, рандомно

    def click_random_checkbox(self):
        # нам нужно много элементов
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)  # тут хранятся все наши элементы чек-бокса
        # item = item_list[random.randint(1, 15)]  # случайно кликаем на один из элементов
        # self.go_to_element(item)  # переходим к элементу, он может быть внизу
        # item.click()
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        # тут нам не надо кликать на элемент, надо просто чтобы он был в DOM-дереве
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        # хотим отобрать нужные элементы и заунуть их в список
        data = []
        for box in checked_list:
            # нужно получить текст рядом с чек-боксом.
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            # добавляем эти элементы, которые рядом с чек-боксом, в массив
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
