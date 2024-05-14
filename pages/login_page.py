import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocator


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 10)

        self.account_link_xpath = LoginLocator.account_xpath
        self.username_css_selector = LoginLocator.username_css_selector
        self.password_css_selector = LoginLocator.password_css_selector
        self.login_button_xpath = LoginLocator.login_button_xpath
        self.logout_xpath = LoginLocator.logout_xpath
        self.error_xpath = LoginLocator.error_xpath

    def go_to_account(self):
        account_link = self.driver.find_element(By.XPATH, self.account_link_xpath)
        account_link.click()

    def login(self, username, password):
        username_input = self.driver.find_element(By.CSS_SELECTOR, self.username_css_selector)
        password_input = self.driver.find_element(By.CSS_SELECTOR, self.password_css_selector)
        login_button = self.driver.find_element(By.XPATH, self.login_button_xpath)

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        self.driver.implicitly_wait(10)
        expected_url = "https://skleptest.pl/my-account/"
        if self.driver.current_url == expected_url:
            print("Clicking the login button took us to the expected page: https://skleptest.pl/my-account/.")
        else:
            print("Error: Clicking the login button did not take us to the expected page.")

    def is_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.logout_xpath)))
            return True
        except:
            return False

    def logout(self):
        logout = self.driver.find_element(By.XPATH, self.logout_xpath)
        logout.click()

        self.driver.implicitly_wait(10)
        expected_url = "https://skleptest.pl/"
        if self.driver.current_url == expected_url:
            print("Clicking the logout button took us to the expected page: https://skleptest.pl/.")
        else:
            print("Error: Clicking the logout button did not take us to the expected page.")

    def is_error_message_displayed(self) -> object:
        try:
            error_message_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_xpath)))
            error_message = error_message_element.text
            self.logger.info(f"Error message displayed: {error_message}")
            return error_message
        except TimeoutException:
            self.logger.error("Timeout: Error message was not visible.")
            return None
