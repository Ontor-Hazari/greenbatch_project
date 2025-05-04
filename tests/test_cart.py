from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_item_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    cart_page = CartPage(page)

    login_page.login("standard_user", "secret_sauce")
    cart_page.add_item_to_cart()
    cart_page.go_to_cart()
    assert cart_page.is_item_in_cart()
