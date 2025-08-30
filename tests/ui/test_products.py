import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.menu_page import MenuPage

@pytest.mark.ui
def test_products_display(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductsPage(driver)
    products = products_page.get_all_products()
    assert len(products) > 0

@pytest.mark.ui
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    assert products_page.get_cart_count() == "1"

@pytest.mark.ui
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    menu_page = MenuPage(driver)
    menu_page.open_menu()
    menu_page.logout()
    
    assert "https://www.saucedemo.com/" in driver.current_url

@pytest.mark.ui
def test_sort_products_by_price(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.sort_by_price_low_to_high()
    prices = products_page.get_prices()
    assert prices == sorted(prices)



