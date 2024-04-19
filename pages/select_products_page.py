from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.select_products_locators import SelectProductsLocator


class SelectProducts:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.select_products_locators = {
            "first_product": SelectProductsLocator.select_first_product_xpath,
            "second_product": SelectProductsLocator.select_second_product_xpath,
            "third_product": SelectProductsLocator.select_third_product_xpath,
            "fourth_product": SelectProductsLocator.select_fourth_product_xpath,
            "fifth_product": SelectProductsLocator.select_fifth_product_xpath,
            "sixth_ product": SelectProductsLocator.select_sixth_product_xpath
        }

    def select_product(self, product_key):
        product_locator = self.select_products_locators.get(product_key)
        if product_locator:
            product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, product_locator)))
            product_link.click()
        else:
            print(f"Product locator not found for product: {product_key}")