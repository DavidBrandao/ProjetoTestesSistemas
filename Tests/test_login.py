import pytest

from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class TestLogin:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        #Login Page Instance
        self.login_page = LoginPage(browser=browser)

        #Open Login Page
        self.login_page.open_login_page()

    # Verify error message for trying to log in without user and password
    def test_click_login_btn(self, setup, tear_down):
        self.login_page.click_login_button()
        error_message = self.login_page.get_login_error_message()
        assert error_message == self.login_page.txtloginErrorMessage, 'Wrong Message'

    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
