import pytest
import datetime
from selenium import webdriver
from pages.categories_page import ProductsCategories
from pages.sort_page import SortPage
from pages.select_products_page import SelectProducts
from pages.add_products_page import AddProducts


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://skleptest.pl")
    yield driver
    driver.quit()


def test_add_shirts(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Shirts")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Popularity")
    select_products = SelectProducts(driver)
    select_products.select_product("first_product")
    add_products = AddProducts(driver)
    add_products.enter_quantity(1)
    add_products.add_to_cart(["add_manago_shirt", "add_alani_shirt", "add_amari_shirt", "add_visual_shirt", "add_marina_style", "add_belka_shirt"])


def test_add_scarfs(driver):
    product_categories = ProductsCategories(driver)
    product_categories.navigate_to_categories()
    product_categories.click_category("Scarfs")
    sorting_option = SortPage(driver)
    sorting_option.locate_sorting_box()
    sorting_option.click_sorting_option("Newness")
    select_products = SelectProducts(driver)
    select_products.select_product("second_product")
    add_products = AddProducts(driver)
    add_products.enter_quantity(2)
    add_products.add_to_cart(["add_andora_scarf", "add_istwic_scarf", "add_jennifer_scarf"])
    add_products.click_my_cart_link()


@pytest.fixture(scope="function", autouse=True)
def screenshot_after_test(request, driver):
    yield
    test_method_name = request.node.name
    timestamp = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = f'../screenshots/test_case_005_{test_method_name}_{timestamp}_pytest.png'
    driver.save_screenshot(screenshot_path)