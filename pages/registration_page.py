import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.registration_locators import Registration

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.account_xpath = Registration.account_xpath
        self.reg_email_css_selector = Registration.reg_email_css_selector
        self.reg_password_css_selector = Registration.reg_password_css_selector
        self.reg_button_xpath = Registration.reg_button_xpath

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

    def check_registration_success(self):
        try:
            success_message = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Hello")
            )
            return True
        except:
            return False
