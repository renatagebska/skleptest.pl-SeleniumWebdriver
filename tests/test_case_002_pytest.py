import pytest
import datetime
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://skleptest.pl")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


def test_login_and_logout(login_page):
    login_page.go_to_account()
    login_page.login("user@example.com", "password1234!!!user")

    assert login_page.is_logged_in()

    login_page.logout()

    assert not login_page.is_logged_in()


def test_login_failed_no_username(login_page):
    login_page.go_to_account()
    login_page.login("", "password1234!!!user")

    error_message = login_page.is_error_message_displayed()
    assert error_message == "Error: Username is required."


def test_login_failed_wrong_username(login_page):
    login_page.go_to_account()
    login_page.login("wrongusername", "password1234!!!user")

    error_message = login_page.is_error_message_displayed()
    assert error_message == 'Error: The username wrongusername is not registered on this site. If you are unsure of your username, try your email address instead.'

def test_login_failed_no_password(login_page):
    login_page.go_to_account()
    login_page.login("user@example.com", "")

    error_message = login_page.is_error_message_displayed()
    assert error_message == "Error: The password field is empty."


def test_login_failed_wrong_password(login_page):
    login_page.go_to_account()
    login_page.login("user@example.com", "somewrongpassword")

    error_message = login_page.is_error_message_displayed()
    assert (error_message == 'Error: The password you entered for the username user@example.com is incorrect. '
                             'Lost your password?')


@pytest.fixture(scope="function", autouse=True)
def screenshot_after_test(request, driver):
    yield
    test_method_name = request.node.name
    timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = f'../screenshots/test_case_002_{test_method_name}_{timestamp}_pytest.png'
    driver.save_screenshot(screenshot_path)