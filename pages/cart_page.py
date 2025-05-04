class CartPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack_button = "[data-test=\"add-to-cart-sauce-labs-backpack\"]"
        self.cart_icon = "[data-test=\"shopping-cart-link\"]"
        self.cart_item = ".cart_item"

    def add_item_to_cart(self):
        self.page.click(self.add_backpack_button)

    def go_to_cart(self):
        self.page.click(self.cart_icon)

    def is_item_in_cart(self):
        return self.page.is_visible(self.cart_item)
