import time

import pytest

from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage
from Pages.ProductsPage import ProductsPage

class Test3:


    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)

        # Open Login Page
        self.login_page.open_login_page()

        # Log Into website
        self.login_page.login()

    # Verify if the user is redirected to product page after login
    def test_logout(self, setup, tear_down):
        # Menu Page Instance
        self.menu_page = MenuPage(self.login_page.driver)

        # Open Sidebar
        self.menu_page.open_menu_sidebar()

        # Click Logout Option
        self.menu_page.click_logout_option()

        # Verify Login Button Is Visible
        is_button_visible = self.login_page.is_login_button_visible()
        assert is_button_visible == True

    @pytest.fixture()
    def tear_down(self):
        yield
        self.menu_page.QuitDriver()