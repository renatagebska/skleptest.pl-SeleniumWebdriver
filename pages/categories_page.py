from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.categories_locators import CategoriesLocator


class ProductsCategories:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Use Categories class attributes to define category IDs
        self.categories = {
            "All": CategoriesLocator.all_id,
            "Shirts": CategoriesLocator.shirts_id,
            "Featured": CategoriesLocator.featured_id,
            "Trends": CategoriesLocator.trends_id,
            "Scarfs": CategoriesLocator.scarfs_id,
            "Shoes": CategoriesLocator.shoes_id,
            "Tops": CategoriesLocator.tops_id,
            "Blouses": CategoriesLocator.blouses_id,
            "Jeans": CategoriesLocator.jeans_id,
            "Dresses": CategoriesLocator.dresses_id
        }

    def navigate_to_categories(self):
        # Find the categories element
        categories_element = self.wait.until(EC.visibility_of_element_located((By.ID, CategoriesLocator.categories_id)))
        # Move to the categories element
        ActionChains(self.driver).move_to_element(categories_element).perform()

    def click_category(self, category):
        # Click on the category
        category_id = self.categories.get(category)
        if category_id:
            try:
                category_element = self.wait.until(EC.visibility_of_element_located((By.ID, category_id)))
                category_element.click()
            except:
                print(f"Failed to click on category: {category}. Element not found.")
        else:
            print(f"Category ID not found for category: {category}")

    def verify_category_navigation(self, category, category_url):
        # Check if URL matches
        if self.driver.current_url != category_url:
            print(f'Failed to navigate to category: {category}')
            return False
        return True