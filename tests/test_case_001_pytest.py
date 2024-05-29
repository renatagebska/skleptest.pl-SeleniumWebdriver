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

    global_email = registration_page.generate_random_email()
    global_password = registration_page.generate_random_password()
    registration_page.input_registration_email_address(global_email)
    registration_page.input_registration_password(global_password)
    registration_page.click_register_button()

    registration_page.is_welcome_element_displayed()


def test_registration_failed_no_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_registration_page()

    registration_page.click_register_button()
    registration_page.is_welcome_element_displayed()

    error_message = registration_page.is_error_message_displayed()
    assert error_message == "Error: Please provide a valid email address.", "Failed: No email error message displayed."


def test_registration_failed_no_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_registration_page()

    global_email = registration_page.generate_random_email()
    registration_page.input_registration_email_address(global_email)
    registration_page.click_register_button()
    registration_page.is_welcome_element_displayed()

    error_message = registration_page.is_error_message_displayed()
    assert error_message == "Error: Please enter an account password.", "Failed: No password error message displayed."


@pytest.fixture(scope="function", autouse=True)
def screenshot_after_test(request, driver):
    yield
    test_method_name = request.node.name
    timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = f'../screenshots/test_case_001_{test_method_name}_{timestamp}_pytest.png'
    driver.save_screenshot(screenshot_path)
