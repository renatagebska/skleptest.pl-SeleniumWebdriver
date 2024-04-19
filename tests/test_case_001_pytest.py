import pytest
import datetime
from selenium import webdriver
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
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


@pytest.fixture(scope="function", autouse=True)
def screenshot_after_test(request, driver):
    yield
    test_method_name = request.node.name
    timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = f'../screenshots/test_case_001_{test_method_name}_{timestamp}_pytest.png'
    driver.save_screenshot(screenshot_path)