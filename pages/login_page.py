import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.login_locators import Login


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 10)

        self.account_link_xpath = Login.account_xpath
        self.username_css_selector = Login.username_css_selector
        self.password_css_selector = Login.password_css_selector
        self.login_button_xpath = Login.login_button_xpath
        self.logout_xpath = Login.logout_xpath

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

    def is_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.logout_xpath)))
            return True
        except:
            return False

    def logout(self):
        logout = self.driver.find_element(By.XPATH, self.logout_xpath)
        logout.click()