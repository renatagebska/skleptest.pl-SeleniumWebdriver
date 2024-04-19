import unittest
import datetime
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
        test_method_name = self._testMethodName
        timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        screenshot_path = f'../screenshots/test_case_002_{test_method_name}_{timestamp}_unittest.png'
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()