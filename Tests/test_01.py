import time

import pytest
from Pages.General import General
from Pages.LoginPage import LoginPage



class TestLogin:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        #Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()

    # Verify error message for trying to log in without user and password
    def test_login_banco(self, setup, tear_down):
        # Logando na aplicação
        self.login_page.login()


    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
