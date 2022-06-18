import time

import pytest

from Pages.LoginPage import LoginPage
from Pages.TransferPage import TransferPage


class Test06:
    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()
        # Logando na aplicação
        self.login_page.login()

    def teste_verificar_transferencia_fundos(self, setup, tear_down):
        # Instanciar a classe transfer
        self.transfer = TransferPage(self.login_page.driver)

        # Acessar e verificar a tela de transfer funds
        assert self.transfer.open_transfer_page()

        # Realizar transferencia para mesma conta
        self.transfer.transfer_funds_same_account()

        # Verificar transferencia relaizada com sucesso
        assert self.transfer.verify_title_sucess()

        # Verificar se dados da transferencia são mostrados na tela
        assert self.transfer.verify_transfer_data_visible()



    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()