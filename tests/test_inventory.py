from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_loaded(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_inventory_loaded()
