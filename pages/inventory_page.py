class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_container = ".inventory_list"

    def is_inventory_loaded(self):
        return self.page.is_visible(self.inventory_container)
