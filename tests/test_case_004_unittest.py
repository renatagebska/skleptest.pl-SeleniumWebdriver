import unittest
import datetime
from selenium import webdriver
from pages.sort_page import SortPage
from pages.categories_page import ProductsCategories


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.product_categories = ProductsCategories(self.driver)
        self.sorting_option = SortPage(self.driver)
        self.product_categories.navigate_to_categories()
        self.product_categories.click_category("Shirts")

    def test_sort_by_popularity(self):
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Popularity")
        self.assertTrue(self.sorting_option.verify_sorting_option("Popularity", "https://skleptest.pl/product-category/shirts/?orderby=popularity"), "Sorting by popularity failed" )

    def test_sort_by_rating(self):
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Rating")
        self.assertTrue(self.sorting_option.verify_sorting_option("Rating", "https://skleptest.pl/product-category/shirts/?orderby=rating"), "Sorting by rating failed")

    def test_sort_by_newness(self):
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Newness")
        self.assertTrue(self.sorting_option.verify_sorting_option("Newness", "https://skleptest.pl/product-category/shirts/?orderby=date"), "Sorting by newness failed")

    def test_sort_by_price_low(self):
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Price_low")
        self.assertTrue(self.sorting_option.verify_sorting_option("Price_low", "https://skleptest.pl/product-category/shirts/?orderby=price"), "Sorting by price low to high failed")

    def test_sort_by_price_high(self):
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Price_high")
        self.assertTrue(self.sorting_option.verify_sorting_option("Price_high", "https://skleptest.pl/product-category/shirts/?orderby=price-desc"), "Sorting by price high to low failed")

    def test_sort_by_default(self):
        self.sorting_option.locate_sorting_box()
        self.sorting_option.click_sorting_option("Default")
        self.assertTrue(self.sorting_option.verify_sorting_option("Default", "https://skleptest.pl/product-category/shirts/?orderby=menu_order"), "Sorting by default sorting failed")

    def tearDown(self):
        test_method_name = self._testMethodName
        timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        screenshot_path = f'../screenshots/test_case_004_{test_method_name}_{timestamp}_unittest.png'
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()