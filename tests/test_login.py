from pages.login_page import LoginPage

def test_login(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    ## Perform login
    login_page.login("standard_user", "secret_sauce")
    
