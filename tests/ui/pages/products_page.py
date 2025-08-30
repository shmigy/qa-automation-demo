from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products = (By.CLASS_NAME, "inventory_item")
        self.add_buttons = (By.CSS_SELECTOR, ".inventory_item button")
        self.sort_select = (By.CLASS_NAME, "product_sort_container")
        self.prices = (By.CLASS_NAME, "inventory_item_price")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_all_products(self):
        return self.driver.find_elements(*self.products)

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.add_buttons)[0].click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def sort_by_price_low_to_high(self):
        select = Select(self.driver.find_element(*self.sort_select))
        select.select_by_value("lohi")

    def get_prices(self):
        price_elements = self.driver.find_elements(*self.prices)
        return [float(p.text.replace("$", "")) for p in price_elements]
