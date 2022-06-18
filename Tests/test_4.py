import time

import pytest

from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage
from Pages.ProductsPage import ProductsPage


class Test4:

    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)

        # Products Page Instance
        self.products_page = ProductsPage(self.login_page.driver)

        # Open Login Page
        self.login_page.open_login_page()

        # Log Into website
        self.login_page.login()

        # Add any product
        self.products_page.add_first_product()
        assert self.products_page.verify_backpack_remove_btn_visible()

    # Verify if the user is redirected to product page after login
    def test_checkout_info(self, setup, tear_down):
        # Cart Page Instance
        self.cart_page = CartPage(self.login_page.driver)

        # Checkout Page Instance
        self.checkout_page = CheckoutPage(self.login_page.driver)

        # Open cart page
        self.cart_page.click_cart_button()

        # Go to Checkout page
        self.cart_page.click_checkout_button()

        # Verify Checkout page title
        page_title = self.checkout_page.get_page_title()
        assert page_title == self.checkout_page.checkoutTitle

        # Click Continue Button
        self.checkout_page.click_continue_button()

        # Verify Error Message
        error_message = self.checkout_page.get_error_message()
        assert error_message == self.checkout_page.errorMessage

    @pytest.fixture()
    def tear_down(self):
        yield
        self.products_page.QuitDriver()
