import pytest

from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage

class TestProducts:


    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)

        # Products Page Instance
        self.products_page = ProductsPage(self.login_page.driver)

        # Open Login Page
        self.login_page.open_login_page()

    # Verify if the user is redirected to product page after login
    def test_login_redirects_products(self, setup, tear_down):
        self.login_page.login()
        page_title = self.products_page.get_page_tile_after_login()
        assert page_title == self.products_page.txtProducts


    @pytest.fixture()
    def tear_down(self):
        yield
        self.products_page.QuitDriver()