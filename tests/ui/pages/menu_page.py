from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def open_menu(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

    def logout(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
