from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')  # решетка - это id
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')
    CREATED_SUBMIT = (By.CSS_SELECTOR, '#output #permanentAddress')




