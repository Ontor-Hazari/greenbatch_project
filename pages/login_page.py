class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "[data-test=\"username\"]"
        self.password_input = "[data-test=\"password\"]"
        self.login_button = "[data-test=\"login-button\"]"

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
