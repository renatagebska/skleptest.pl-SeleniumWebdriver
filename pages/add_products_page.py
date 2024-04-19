from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.add_products_locators import MyCartLocator, QuantityLocator, AddProductsLocator


class AddProducts:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.cart_link_css = MyCartLocator.cart_link_css
        self.quantity_input = QuantityLocator.quantity_input_css_selector

        self.add_to_cart_locators = {
            "add_manago_shirt": AddProductsLocator.add_manago_shirt_css,
            "add_alani_shirt": AddProductsLocator.add_alani_shirt_css,
            "add_amari_shirt": AddProductsLocator.add_amari_shirt_css,
            "add_visual_shirt": AddProductsLocator.add_visual_shirt_css,
            "add_marina_style": AddProductsLocator.add_marina_style_css,
            "add_belka_shirt": AddProductsLocator.add_belka_shirt_css,
            "add_andora_scarf": AddProductsLocator.add_andora_scarf_css,
            "add_istwic_scarf": AddProductsLocator.add_istwic_scarf_css,
            "add_jennifer_scarf": AddProductsLocator.add_jennifer_scarf_css,
            "add_beije_magawi_shoes": AddProductsLocator.add_beije_magawi_shoes_css,
            "add_blue_magawi_shoes": AddProductsLocator.add_blue_magawi_shoes_css,
            "add_red_magawi_shoes": AddProductsLocator.add_red_magawi_shoes_css,
            "add_black_top": AddProductsLocator.add_black_top_css,
            "add_little_black_top": AddProductsLocator.add_little_black_top_css,
            "add_magnolia_dress": AddProductsLocator.add_magnolia_dress_css,
            "add_marcara_sleeveless_dress": AddProductsLocator.add_marcara_sleeveless_dress_css,
            "add_blue_sweater": AddProductsLocator.add_blue_sweater_css,
            "add-merchantile_blouse": AddProductsLocator.add_merchantile_blouse_css,
            "add_asabi_jeans": AddProductsLocator.add_asabi_jeans_css,
            "add_rocadi_jeans": AddProductsLocator.add_rocadi_jeans_css,
            "add_fitt_belts": AddProductsLocator.add_fitt_belts_css
        }

    def enter_quantity(self, quantity):
        quantity_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys(quantity)

    def add_to_cart(self, product_keys):
        for product_key in product_keys:
            add_to_cart_locator = self.add_to_cart_locators.get(product_key)
            if add_to_cart_locator:
                try:
                    add_to_cart_button = self.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, add_to_cart_locator)))
                    add_to_cart_button.click()
                    print(f"Added product to cart: {product_key}")
                    break  # Exit the loop after successfully adding the product
                except Exception as e:
                    print(f"Failed to add product to cart: {product_key}. Error: {str(e)}")
            else:
                print(f"Add to cart button locator not found for product: {product_key}")

    def click_my_cart_link(self):
        my_cart_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.cart_link_css)))
        my_cart_link.click()

        self.driver.implicitly_wait(10)
        expected_url = "https://skleptest.pl/cart/"
        if self.driver.current_url == expected_url:
            print("Clicking the cart link took us to the expected page: https://skleptest.pl/cart/.")
        else:
            print("Error: Clicking the cart link did not take us to the expected page.")