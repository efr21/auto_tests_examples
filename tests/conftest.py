import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
