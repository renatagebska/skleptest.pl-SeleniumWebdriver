import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.login_page = LoginPage(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_and_logout(self):
        self.login_page.go_to_account()
        self.login_page.login("user@example.com", "password1234!!!user")

        self.assertTrue(self.login_page.is_logged_in())

        self.login_page.logout()

        self.assertFalse(self.login_page.is_logged_in())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()