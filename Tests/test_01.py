import time

import pytest
from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.OpenAccountPage import OpenAccountPage

class TestLogin:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        #Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()


    def test_login_banco(self, setup, tear_down):
        # Logando na aplicação
        self.login_page.login()

        # Acessar a pagina New Account
        self.open_account_page = OpenAccountPage(self.login_page.driver)
        assert self.open_account_page.open_new_account_page(), 'O site não se encontra na criação de conta !'

        #Clicando no botão criar conta
        self.open_account_page.create_new_account()

        time.sleep(5)


    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
