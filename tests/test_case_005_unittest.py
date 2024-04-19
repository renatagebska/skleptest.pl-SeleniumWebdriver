import unittest
import datetime
from selenium import webdriver
from pages.categories_page import ProductsCategories
from pages.sort_page import SortPage
from pages.select_products_page import SelectProducts
from pages.add_products_page import AddProducts


class TestAddProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.product_categories = ProductsCategories(self.driver)
        self.sorting_option = SortPage(self.driver)
        self.select_products = SelectProducts(self.driver)
        self.add_products = AddProducts(self.driver)

    def test_add_shirts(self):
        self.product_categories.navigate_to_categories()
        self.product_categories.click_category("Shirts")
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Popularity")
        self.select_products.select_product("first_product")
        self.add_products.enter_quantity(1)
        self.add_products.add_to_cart(["add_manago_shirt", "add_alani_shirt", "add_amari_shirt", "add_visual_shirt", "add_marina_style", "add_belka_shirt"])

    def test_add_scarfs(self):
        self.product_categories.navigate_to_categories()
        self.product_categories.click_category("Scarfs")
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Newness")
        self.select_products.select_product("second_product")
        self.add_products.enter_quantity(2)
        self.add_products.add_to_cart(["add_andora_scarf", "add_istwic_scarf", "add_jennifer_scarf"])
        self.add_products.click_my_cart_link()

    def tearDown(self):
        test_method_name = self._testMethodName
        timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        screenshot_path = f'../screenshots/test_case_005_{test_method_name}_{timestamp}_unittest.png'
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()