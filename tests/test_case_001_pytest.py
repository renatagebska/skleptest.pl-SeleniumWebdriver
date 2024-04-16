import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://skleptest.pl")
    yield driver
    driver.quit()

def test_registration_successful(driver):
    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_registration_page()
    registration_page.enter_registration_details("example45@example.com", "exAMPLEpasswor33d124!!")
    registration_page.click_register_button()