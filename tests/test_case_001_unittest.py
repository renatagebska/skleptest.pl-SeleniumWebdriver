import unittest
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

        global_email = registration_page.generate_random_email()
        global_password = registration_page.generate_random_password()

        registration_page.input_registration_email_address(global_email)
        registration_page.input_registration_password(global_password)

        registration_page.click_register_button()
        registration_page.is_welcome_element_displayed()

    def test_registration_failed_no_email(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.navigate_to_registration_page()

        registration_page.click_register_button()
        registration_page.is_welcome_element_displayed()

        error_message = registration_page.is_error_message_displayed()
        self.assertEqual(error_message, 'Error: Please provide a valid email address.')

    def test_registration_failed_no_password(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.navigate_to_registration_page()

        global_email = registration_page.generate_random_email()
        registration_page.input_registration_email_address(global_email)

        registration_page.click_register_button()
        registration_page.is_welcome_element_displayed()

        error_message = registration_page.is_error_message_displayed()
        self.assertEqual(error_message, 'Error: Please enter an account password.')

    def tearDown(self):
        test_method_name = self._testMethodName
        timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        screenshot_path = f'../screenshots/test_case_001_{test_method_name}_{timestamp}_unittest.png'
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()