import logging
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.registration_locators import RegistrationLocator
import random
import string


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        self.wait = WebDriverWait(self.driver, 10)

        self.account_xpath = RegistrationLocator.account_xpath
        self.reg_email_css_selector = RegistrationLocator.reg_email_css_selector
        self.reg_password_css_selector = RegistrationLocator.reg_password_css_selector
        self.reg_button_xpath = RegistrationLocator.reg_button_xpath
        self.error_xpath = RegistrationLocator.error_xpath
        self.welcome_element_class = RegistrationLocator.welcome_element_class

    def navigate_to_registration_page(self):
        try:
            account_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.account_xpath)))
            account_element.click()
        except TimeoutException:
            self.logger.error("Timeout: Registration page navigation took too long.")

    def generate_random_email(self):
        email_prefix = "example"
        email_domain = "example.com"
        random_string_length = 10
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random_string_length))
        return f"{email_prefix}_{random_string}@{email_domain}"

    def generate_random_password(self):
        password_length = 12
        all_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.sample(all_chars, password_length))

    def input_registration_email_address(self, reg_email):
        try:
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.reg_email_css_selector)))
            email_input.clear()
            email_input.send_keys(reg_email)
        except TimeoutException:
            self.logger.error("Timeout: Email input field was not visible.")

    def input_registration_password(self, reg_password):
        try:
            password_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.reg_password_css_selector)))
            password_input.clear()
            password_input.send_keys(reg_password)
        except TimeoutException:
            self.logger.error("Timeout: Password input field was not visible.")

    def click_register_button(self):
        try:
            reg_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.reg_button_xpath)))
            reg_button.click()
        except TimeoutException:
            self.logger.error("Timeout: Register button was not clickable.")

    def is_welcome_element_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.welcome_element_class)))
            return True
        except TimeoutException:
            self.logger.error("Timeout: Welcome element was not visible.")
            return False

    def is_error_message_displayed(self) -> object:
        try:
            error_message_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_xpath)))
            error_message = error_message_element.text
            self.logger.info(f"Error message displayed: {error_message}")
            return error_message
        except TimeoutException:
            self.logger.error("Timeout: Error message was not visible.")
            return None
