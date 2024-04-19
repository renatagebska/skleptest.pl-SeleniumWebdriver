import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.registration_locators import RegistrationLocator


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.account_xpath = RegistrationLocator.account_xpath
        self.reg_email_css_selector = RegistrationLocator.reg_email_css_selector
        self.reg_password_css_selector = RegistrationLocator.reg_password_css_selector
        self.reg_button_xpath = RegistrationLocator.reg_button_xpath

    def navigate_to_registration_page(self):
        self.driver.find_element(By.XPATH, self.account_xpath).click()

    def enter_registration_details(self, email, password):
        email_input = self.driver.find_element(By.CSS_SELECTOR, self.reg_email_css_selector)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.CSS_SELECTOR, self.reg_password_css_selector)
        password_input.clear()
        password_input.send_keys(password)

    def click_register_button(self):
        self.driver.find_element(By.XPATH, self.reg_button_xpath).click()
        self.driver.implicitly_wait(10)
        expected_url = "https://skleptest.pl/my-account/"
        if self.driver.current_url == expected_url:
            print("Clicking the registration button took us to the expected page: https://skleptest.pl/my-account/.")
        else:
            print("Error: Clicking the registration button did not take us to the expected page.")