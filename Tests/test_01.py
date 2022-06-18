import time
import pytest
from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.OpenAccountPage import OpenAccountPage

class Test01:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        #Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()

    def test_criar_nova_conta(self, setup, tear_down):
        # Logando na aplicação
        self.login_page.login()

        # Acessar a pagina New Account
        self.open_account_page = OpenAccountPage(self.login_page.driver)
        assert self.open_account_page.open_new_account_page(), 'O site não se encontra na criação de conta !'

        # Clicando nova conta e retornando seu numero
        self.numero_conta = self.open_account_page.create_new_account()

        # Validando que o numero da conta é um inteiro
        assert type(self.numero_conta) is int

    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
