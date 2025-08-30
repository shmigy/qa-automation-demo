import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
def test_login_valid(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


@pytest.mark.ui
def test_login_invalid(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid_user", "wrong_pass")
    assert "Username and password do not match" in login_page.get_error()

