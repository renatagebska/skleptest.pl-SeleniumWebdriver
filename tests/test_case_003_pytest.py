import pytest
import datetime
from selenium import webdriver
from pages.categories_page import ProductsCategories


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://skleptest.pl")
    yield driver
    driver.quit()


def test_all_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    # Navigate to the categories link
    product_categories.navigate_to_categories()
    # Click on the "All" category
    product_categories.click_category("All")
    # Verify navigation for the "All" category
    assert product_categories.verify_category_navigation("All", "https://skleptest.pl/shop/"), "Navigation to All category failed"


def test_shirts_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    assert product_categories.verify_category_navigation("Shirts","https://skleptest.pl/product-category/shirts/"), "Navigation to Shirts category failed"


def test_featured_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Featured")
    assert product_categories.verify_category_navigation("Featured", "https://skleptest.pl/product-category/featured/"), "Navigation to Featured category failed"


def test_trends_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Trends")
    assert product_categories.verify_category_navigation("Trends", "https://skleptest.pl/product-category/trends/"), "Navigation to Trends category failed"


def test_scarfs_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Scarfs")
    assert product_categories.verify_category_navigation("Scarfs", "https://skleptest.pl/product-category/scarfs/"), "Navigation to Scarfs category failed"


def test_shoes_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shoes")
    assert product_categories.verify_category_navigation("Shoes", "https://skleptest.pl/product-category/shoes/"), "Navigation to Shoes category failed"


def test_tops_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Tops")
    assert product_categories.verify_category_navigation("Tops", "https://skleptest.pl/product-category/tops/"), "Navigation to Tops category failed"


def test_blouses_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Blouses")
    assert product_categories.verify_category_navigation("Blouses", "https://skleptest.pl/product-category/blouse/"), "Navigation to Blouses category failed"


def test_jeans_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Jeans")
    assert product_categories.verify_category_navigation("Jeans", "https://skleptest.pl/product-category/jeans/"), "Navigation to Jeans category failed"


def test_dresses_category_navigation(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Dresses")
    assert product_categories.verify_category_navigation("Dresses", "https://skleptest.pl/product-category/dresses/"), "Navigation to Dresses category failed"


@pytest.fixture(scope="function", autouse=True)
def screenshot_after_test(request, driver):
    yield
    test_method_name = request.node.name
    timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = f'../screenshots/test_case_003_{test_method_name}_{timestamp}_pytest.png'
    driver.save_screenshot(screenshot_path)