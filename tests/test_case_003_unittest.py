import unittest
from selenium import webdriver
from pages.categories_page import ProductsCategories


class TestCategoryNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.product_categories = ProductsCategories(self.driver)

    def test_all_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "All" category
        self.product_categories.click_category("All")
        # Verify navigation for the "All" category
        self.assertTrue(self.product_categories.verify_category_navigation("All", "https://skleptest.pl/shop/"), "Navigation to All category failed")

    def test_shirts_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Shirts" category
        self.product_categories.click_category("Shirts")
        # Verify navigation for the "Shirts" category
        self.assertTrue(self.product_categories.verify_category_navigation("Shirts", "https://skleptest.pl/product-category/shirts/"), "Navigation to Shirts category failed")

    def test_featured_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Featured" category
        self.product_categories.click_category("Featured")
        # Verify navigation for the "Featured" category
        self.assertTrue(self.product_categories.verify_category_navigation("Featured", "https://skleptest.pl/product-category/featured/"), "Navigation to Featured category failed")

    def test_trends_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Trends" category
        self.product_categories.click_category("Trends")
        # Verify navigation for the "Trends" category
        self.assertTrue(self.product_categories.verify_category_navigation("Trends", "https://skleptest.pl/product-category/trends/"), "Navigation to Trends category failed")

    def test_scarfs_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Scarfs" category
        self.product_categories.click_category("Scarfs")
        # Verify navigation for the "Scarfs" category
        self.assertTrue(self.product_categories.verify_category_navigation("Scarfs", "https://skleptest.pl/product-category/scarfs/"), "Navigation to Scarfs category failed")

    def test_shoes_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Shoes" category
        self.product_categories.click_category("Shoes")
        # Verify navigation for the "Shoes" category
        self.assertTrue(self.product_categories.verify_category_navigation("Shoes", "https://skleptest.pl/product-category/shoes/"), "Navigation to Shoes category failed")

    def test_tops_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Tops" category
        self.product_categories.click_category("Tops")
        # Verify navigation for the "Tops" category
        self.assertTrue(self.product_categories.verify_category_navigation("Tops", "https://skleptest.pl/product-category/tops/"), "Navigation to Tops category failed")

    def test_blouses_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Blouses" category
        self.product_categories.click_category("Blouses")
        # Verify navigation for the "Blouses" category
        self.assertTrue(self.product_categories.verify_category_navigation("Blouses", "https://skleptest.pl/product-category/blouse/"), "Navigation to Blouses category failed")

    def test_jeans_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Jeans" category
        self.product_categories.click_category("Jeans")
        # Verify navigation for the "Jeans" category
        self.assertTrue(self.product_categories.verify_category_navigation("Jeans", "https://skleptest.pl/product-category/jeans/"),"Navigation to Jeans category failed")

    def test_dresses_category_navigation(self):
        # Navigate to the categories link
        self.product_categories.navigate_to_categories()
        # Click on the "Dresses" category
        self.product_categories.click_category("Dresses")
        # Verify navigation for the "Dresses" category
        self.assertTrue(self.product_categories.verify_category_navigation("Dresses", "https://skleptest.pl/product-category/dresses/"),"Navigation to Dresses category failed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
