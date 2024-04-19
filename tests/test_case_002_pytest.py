import pytest
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


def test_login_and_logout(driver, login_page):
    login_page.go_to_account()
    login_page.login("user@example.com", "password1234!!!user")

    assert login_page.is_logged_in()

    login_page.logout()

    assert not login_page.is_logged_in()