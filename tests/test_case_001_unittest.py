import unittest
import time
from selenium import webdriver
import datetime
from pages.registration_page import RegistrationPage


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://skleptest.pl/')

    def test_registration_successful(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.navigate_to_registration_page()
        registration_page.enter_registration_details("example2444@example.com", "1222examplepassword1!$")
        registration_page.click_register_button()

    def tearDown(self):
        test_method_name = self._testMethodName
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = f'../screenshots/{test_method_name}_{timestamp}.png'
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
