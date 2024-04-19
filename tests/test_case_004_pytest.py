import pytest
from selenium import webdriver
from pages.categories_page import ProductsCategories
from pages.sort_page import SortPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://skleptest.pl")
    yield driver
    driver.quit()


def test_sort_by_popularity(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Popularity")
    assert sorting_option.verify_sorting_option("Popularity", "https://skleptest.pl/product-category/shirts/?orderby=popularity"), "Sorting by popularity failed"


def test_sort_by_rating(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Rating")
    assert sorting_option.verify_sorting_option("Rating", "https://skleptest.pl/product-category/shirts/?orderby=rating"), "Sorting by rating failed"


def test_sort_by_newness(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Newness")
    assert sorting_option.verify_sorting_option("Newness", "https://skleptest.pl/product-category/shirts/?orderby=date"), "Sorting by newness failed"


def test_sort_by_price_low(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Price_low")
    assert sorting_option.verify_sorting_option("Price_low", "https://skleptest.pl/product-category/shirts/?orderby=price"), "Sorting by price low to high failed"


def test_sort_by_price_high(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Price_high")
    assert sorting_option.verify_sorting_option("Price_high", "https://skleptest.pl/product-category/shirts/?orderby=price-desc"), "Sorting by price high to low failed"


def test_sort_by_default(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Default")
    assert sorting_option.verify_sorting_option("Default", "https://skleptest.pl/product-category/shirts/?orderby=menu_order"), "Sorting by default sorting failed"