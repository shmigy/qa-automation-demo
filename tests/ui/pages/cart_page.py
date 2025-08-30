from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))
