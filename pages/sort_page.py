from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.sort_locators import SortProducts

class SortPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.sorting_box_name = SortProducts.sorting_box_name
        self.default_sorting_xpath = SortProducts.default_sorting_xpath
        self.sort_by_popularity_xpath = SortProducts.sort_by_popularity_xpath
        self.sort_by_rating_xpath = SortProducts.sort_by_rating_xpath
        self.sort_by_newness_xpath = SortProducts.sort_by_newness_xpath
        self.sort_by_price_low_xpath = SortProducts.sort_by_price_low_xpath
        self.sort_by_price_high_xpath = SortProducts.sort_by_price_high_xpath

    def locate_sorting_box(self):
        sorting_box_element = self.wait.until(EC.visibility_of_element_located((By.NAME, self.sorting_box_name)))
        sorting_box_element.click()

    def check_default_sorting(self):
        default_sorting_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.default_sorting_xpath)))
        default_sorting_element.click()

    def check_sort_by_popularity(self):
        sort_by_popularity_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_popularity_xpath)))
        sort_by_popularity_element.click()

    def check_sort_by_rating(self):
        sort_by_rating_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_rating_xpath)))
        sort_by_rating_element.click()

    def check_sort_by_newness(self):
        sort_by_newness_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_newness_xpath)))
        sort_by_newness_element.click()

    def check_sort_by_price_low(self):
        sort_by_price_low_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price_low_xpath)))
        sort_by_price_low_element.click()

    def check_sort_by_price_high(self):
        sort_by_price_high_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price_high_xpath)))
        sort_by_price_high_element.click()

