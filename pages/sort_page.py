from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.sort_locators import SortProductsLocator


class SortPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.sorting_box_name = SortProductsLocator.sorting_box_name
        self.sorting_options = {
            "Default": SortProductsLocator.default_sorting_xpath,
            "Popularity": SortProductsLocator.sort_by_popularity_xpath,
            "Rating": SortProductsLocator.sort_by_rating_xpath,
            "Newness": SortProductsLocator.sort_by_newness_xpath,
            "Price_asc": SortProductsLocator.sort_by_price_low_xpath,
            "Price_desc": SortProductsLocator.sort_by_price_high_xpath
        }

    def locate_sorting_box(self):
        sorting_box_element = self.wait.until(EC.visibility_of_element_located((By.NAME, self.sorting_box_name)))
        sorting_box_element.click()

    def click_sorting_option(self, option):
        sort = self.sorting_options.get(option)
        if sort:
            try:
                sort_by_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, sort)))
                sort_by_element.click()
            except:
                print(f"Failed to click on {option}.")
        else:
            print(f"Sorting option {option} is not valid.")

    def verify_sorting_option(self, option, option_url):
        if self.driver.current_url != option_url:
            print(f"Sorting option {option} does not work.")
            return False
        return True